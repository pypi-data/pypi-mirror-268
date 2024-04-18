#
# Copyright © 2021 United States Government as represented by the Administrator
# of the National Aeronautics and Space Administration. No copyright is claimed
# in the United States under Title 17, U.S. Code. All Other Rights Reserved.
#
# SPDX-License-Identifier: NASA-1.3
#
"""Render an animation of an observing plan."""
import logging

from astropy import units as u
from ligo.skymap.tool import ArgumentParser, FileType

from .. import mission as _mission
from ..units import equivalencies

log = logging.getLogger(__name__)


def parser():
    p = ArgumentParser(prog='dorado-scheduling-animate')

    group = p.add_argument_group(
        'problem setup options',
        'Options that control the problem setup')
    group.add_argument(
        '--mission', choices=set(_mission.__all__) - {'Mission'},
        default='dorado', help='Mission configuration')
    group.add_argument(
        '--delay', type=u.Quantity, default='30 min',
        help='Delay after event time to start observing (any time units)')
    group.add_argument(
        '--duration', type=u.Quantity, default='1 orbit',
        help='Duration of observing plan (any time units)')

    group = p.add_argument_group(
        'discretization options',
        'Options that control the discretization of decision variables')
    group.add_argument(
        '--time-step', type=u.Quantity, default='1 min',
        help='Model time step')

    p.add_argument(
        '--nside', type=int, default=32, help='HEALPix sampling resolution')
    p.add_argument(
        'skymap', metavar='FILE.fits[.gz]', type=FileType('rb'),
        help='Input sky map')
    p.add_argument(
        'schedule', metavar='SCHEDULE.ecsv', type=FileType('rb'), default='-',
        help='Schedule filename')
    p.add_argument(
        'output', metavar='MOVIE.gif', type=FileType('wb'),
        help='Output filename')

    return p


def main(args=None):
    args = parser().parse_args(args)

    # Late imports
    from astropy.coordinates import ICRS
    from astropy_healpix import HEALPix
    from astropy.io import fits
    from astropy.time import Time
    from astropy.table import QTable
    from ligo.skymap.io import read_sky_map
    from ligo.skymap.bayestar import rasterize
    from ligo.skymap import plot
    from ligo.skymap.postprocess import find_greedy_credible_levels
    from matplotlib import pyplot as plt
    from matplotlib.animation import FuncAnimation, PillowWriter
    from matplotlib.ticker import FormatStrFormatter
    import numpy as np
    import seaborn
    from tqdm import tqdm

    mission = getattr(_mission, args.mission)()
    healpix = HEALPix(args.nside, order='nested', frame=ICRS())

    log.info('reading sky map')

    # Read multi-order sky map and rasterize to working resolution
    start_time = Time(fits.getval(args.skymap, 'DATE-OBS', ext=1))
    skymap = read_sky_map(args.skymap, moc=True)['UNIQ', 'PROBDENSITY']
    skymap_hires = rasterize(skymap)['PROB']
    skymap = rasterize(skymap, healpix.level)['PROB']

    cls = find_greedy_credible_levels(skymap_hires)

    with u.add_enabled_equivalencies(equivalencies.orbital(mission.orbit)):
        times = start_time + args.delay + np.arange(
            0, args.duration.to_value(u.s),
            args.time_step.to_value(u.s)) * u.s

    log.info('reading observing schedule')
    schedule = QTable.read(args.schedule.name, format='ascii.ecsv')

    log.info('calculating field of regard')
    field_of_regard = mission.get_field_of_regard(
        healpix.healpix_to_skycoord(np.arange(healpix.npix)), times)

    orbit_field_of_regard = np.logical_or.reduce(field_of_regard)
    continuous_viewing_zone = np.logical_and.reduce(field_of_regard)
    has_continuous_viewing_zone = np.any(continuous_viewing_zone)

    t = (times - times[0]).to(u.minute).value

    (
        instantaneous_color, orbit_color, continuous_color, skymap_color,
        _, footprint_color
    ) = seaborn.color_palette('Paired', n_colors=6)

    fig = plt.figure(figsize=(8, 8))
    gs_sky, gs_time, gs_prob = plt.GridSpec(
        3, 1, height_ratios=[2, 1, 1], hspace=0.1)

    ax_time = fig.add_subplot(gs_time)
    ax_time.set_xlim(t[0], t[-1])
    ax_time.set_ylim(0, 100)
    ax_time.yaxis.set_major_formatter(FormatStrFormatter('%g%%'))
    ax_time.set_ylabel('Fraction of sky')
    twin = ax_time.twinx()
    twin.set_ylim(0, 4 * 180**2 / np.pi * 1e-4)
    twin.set_ylabel('Area ($10^4$ deg$^2$)')
    plt.setp(ax_time.get_xticklabels(), visible=False)

    indices = np.asarray([], dtype=np.intp)
    prob = []
    for row in schedule:
        new_indices = mission.fov.footprint_healpix(
            healpix, row['center'], row['roll'])
        indices = np.unique(np.concatenate((indices, new_indices)))
        prob.append(100 * skymap[indices].sum())

    ax_prob = fig.add_subplot(gs_prob, sharex=ax_time, sharey=ax_time)
    start = (schedule['time'] - times[0]).to_value(u.minute).tolist()
    ax_prob.plot(
        [t[0] - 1] + start + [t[-1] + 1], [0] + prob + [100], '-o',
        drawstyle='steps-post', color='black')
    ax_prob.set_xlabel(f'Time since {start_time.iso} (minutes)')
    ax_prob.set_ylabel('Integrated prob.')

    if has_continuous_viewing_zone:
        y = continuous_viewing_zone.sum() / healpix.npix * 100
        ax_time.axhline(y, color=continuous_color, zorder=2.1)

    y = field_of_regard.sum(1) / healpix.npix * 100
    ax_time.fill_between(
        t, y, np.repeat(100, len(y)), color=instantaneous_color, zorder=2.2)

    y = orbit_field_of_regard.sum() / healpix.npix * 100
    ax_time.axhspan(y, 100, color=orbit_color, zorder=2.3)

    ax_sky = fig.add_subplot(gs_sky, projection='astro hours mollweide')
    ax_sky.grid()
    colors = [continuous_color, orbit_color, instantaneous_color]
    labels = ['Continuous', 'Orbit-averaged', 'Instantaneous']
    if not has_continuous_viewing_zone:
        colors = colors[1:]
        labels = labels[1:]
    ax_sky.add_artist(ax_sky.legend(
        [plt.Rectangle((0, 0), 0, 0, edgecolor='none', facecolor=color)
         for color in colors],
        labels, title='Outside field of regard',
        bbox_to_anchor=[-0.05, -0.3, 1.1, 1.6], loc='upper right'))
    ax_sky.legend(
        [plt.Rectangle((0, 0), 0, 0, edgecolor=color, facecolor='none')
         for color in [skymap_color, footprint_color]],
        ['Localization', 'Observations'],
        bbox_to_anchor=[-0.05, -0.3, 1.1, 1.6], loc='upper left')

    ax_sky.contour_hpx(cls, levels=[0.9], colors=[skymap_color], nested=True)
    if has_continuous_viewing_zone:
        ax_sky.contourf_hpx(continuous_viewing_zone.astype(float),
                            levels=[0, 0.5], colors=[continuous_color],
                            nested=True, zorder=0.3)
    ax_sky.contourf_hpx(orbit_field_of_regard.astype(float), levels=[0, 0.5],
                        colors=[orbit_color], nested=True, zorder=0.5)

    old_artists = []

    log.info('rendering animation frames')
    with tqdm(total=len(field_of_regard)) as progress:

        def animate(i):
            for artist in old_artists:
                artist.remove()
            del old_artists[:]
            for row in schedule:
                if times[i] >= row['time']:
                    poly = mission.fov.footprint(
                        row['center'], row['roll']).icrs
                    vertices = np.column_stack((poly.ra.rad, poly.dec.rad))
                    for cut_vertices in plot.cut_prime_meridian(vertices):
                        patch = plt.Polygon(
                            np.rad2deg(cut_vertices),
                            transform=ax_sky.get_transform('world'),
                            facecolor='none', edgecolor=footprint_color)
                        old_artists.append(ax_sky.add_patch(patch))
            old_artists.extend(ax_sky.contourf_hpx(
                field_of_regard[i].astype(float), levels=[0, 0.5],
                colors=[instantaneous_color], nested=True,
                zorder=0.4).collections)
            old_artists.append(ax_prob.axvline(t[i], color='gray', zorder=10))
            old_artists.append(ax_time.axvline(t[i], color='gray', zorder=10))
            progress.update()

        ani = FuncAnimation(fig, animate, frames=range(len(field_of_regard)))
        ani.save(args.output.name, writer=PillowWriter())


if __name__ == '__main__':
    main()
