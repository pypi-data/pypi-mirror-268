#
# Copyright © 2021 United States Government as represented by the Administrator
# of the National Aeronautics and Space Administration. No copyright is claimed
# in the United States under Title 17, U.S. Code. All Other Rights Reserved.
#
# SPDX-License-Identifier: NASA-1.3
#
"""Plot an observing plan."""
import logging

from ligo.skymap.tool import ArgumentParser, FileType

from .. import mission as _mission

log = logging.getLogger(__name__)


def parser():
    p = ArgumentParser(prog='dorado-scheduling-animate-survey')
    p.add_argument('skymap', metavar='FILE.fits[.gz]',
                   type=FileType('rb'), help='Input sky map')
    p.add_argument('schedule', metavar='SCHEDULE.ecsv',
                   type=FileType('rb'), default='-',
                   help='Schedule filename')
    p.add_argument('--mission', choices=set(_mission.__all__) - {'Mission'},
                   default='dorado', help='Mission configuration')
    p.add_argument('--output', '-o',
                   metavar='MOVIE.gif', type=FileType('wb'),
                   help='Output filename')
    p.add_argument('-s', '--start_time', type=str,
                   default='2020-01-01T00:00:00')
    p.add_argument('-j', '--jobs', type=int, default=1, const=None, nargs='?',
                   help='Number of threads')
    p.add_argument('-n', '--nframes', default=100,
                   type=int, help='Number of frames for movie')
    p.add_argument(
        '--nside', type=int, default=32, help='HEALPix sampling resolution')

    return p


def main(args=None):
    args = parser().parse_args(args)

    # Late imports
    from astropy_healpix import HEALPix, nside_to_level, npix_to_nside
    from astropy.coordinates import ICRS
    from astropy.time import Time
    from astropy.table import QTable
    from astropy import units as u
    from ligo.skymap.io import read_sky_map
    from ligo.skymap.bayestar import rasterize
    from ligo.skymap import plot
    from ligo.skymap.postprocess import find_greedy_credible_levels
    from matplotlib import pyplot as plt
    from matplotlib.animation import FuncAnimation
    from matplotlib.ticker import FormatStrFormatter
    import numpy as np
    import seaborn
    from tqdm import tqdm

    mission = getattr(_mission, args.mission)()
    healpix = HEALPix(args.nside, order='nested', frame=ICRS())

    log.info('reading sky map')
    # Read multi-order sky map and rasterize to working resolution
    start_time = Time(args.start_time, format='isot')
    skymap = read_sky_map(args.skymap, moc=True)['UNIQ', 'PROBDENSITY']
    skymap_hires = rasterize(skymap)['PROB']
    healpix_hires = HEALPix(npix_to_nside(len(skymap_hires)))
    skymap = rasterize(skymap,
                       nside_to_level(healpix.nside))['PROB']
    nest = healpix.order == 'nested'
    if nest:
        skymap = skymap[healpix.ring_to_nested(np.arange(
            len(skymap)))]
        skymap_hires = skymap[healpix_hires.ring_to_nested(np.arange(
            len(skymap_hires)))]

    cls = find_greedy_credible_levels(skymap_hires)

    log.info('reading observing schedule')
    schedule = QTable.read(args.schedule.name, format='ascii.ecsv')

    times = schedule["time"]

    t = (times - times[0]).to(u.minute).value

    nslice = int(len(times)/float(args.nframes))

    instantaneous_color, orbit_color, _, skymap_color, _, footprint_color = \
        seaborn.color_palette('Paired', n_colors=6)

    survey_set = list(set(schedule["survey"]))
    colors = seaborn.color_palette('Set2', n_colors=len(survey_set))

    log.info('reading skymaps')
    clss = []
    skymaps = []
    skymaps_hold = {}
    clss_hold = {}
    for ii, row in enumerate(schedule):
        if np.mod(ii, 100) == 0:
            print('%d/%d' % (ii, len(schedule)))

        survey = row["survey"]
        if (survey not in skymaps_hold) or (survey == "GW"):
            skymap = read_sky_map(row['skymap'],
                                  moc=True)['UNIQ', 'PROBDENSITY']
            skymap_hires = rasterize(skymap)['PROB']
            healpix_hires = HEALPix(npix_to_nside(len(skymap_hires)))
            skymap = rasterize(skymap,
                               nside_to_level(args.nside))
            skymap = skymap['PROB']
            nest = healpix.order == 'nested'
            if not nest:
                skymap = skymap[healpix.ring_to_nested(np.arange(
                    len(skymap)))]
                skymap_hires = skymap[healpix_hires.ring_to_nested(np.arange(
                    len(skymap_hires)))]
            cls = find_greedy_credible_levels(skymap_hires)
            skymaps_hold[survey] = skymap
            clss_hold[survey] = cls

        clss.append(clss_hold[survey])
        skymaps.append(skymaps_hold[survey])
    schedule.add_column(clss, name='cls')
    schedule.add_column(skymaps, name='map')

    log.info('calculating field of regard')
    field_of_regard = mission.get_field_of_regard(
        healpix.healpix_to_skycoord(
            np.arange(healpix.npix)), times[::nslice], jobs=args.jobs)

    orbit_field_of_regard = np.logical_or.reduce(field_of_regard)
    # continuous_viewing_zone = np.logical_and.reduce(field_of_regard)

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
        new_indices = mission.fov.footprint_healpix(healpix, row['center'])
        indices = np.unique(np.concatenate((indices, new_indices)))
        prob.append(100 * skymap[indices].sum())

    ax_prob = fig.add_subplot(gs_prob, sharex=ax_time, sharey=ax_time)
    start = (schedule['time'] - times[0]).to_value(u.minute).tolist()
    ax_prob.plot(
        [t[0] - 1] + start + [t[-1] + 1], [0] + prob + [100], '-o',
        drawstyle='steps-post', color='black')
    ax_prob.set_xlabel(f'Time since {start_time.iso} (minutes)')
    ax_prob.set_ylabel('Integrated prob.')

    y = field_of_regard.sum(1) / healpix.npix * 100
    ax_time.fill_between(
        t[::nslice], y,
        np.repeat(100, len(y)), color=instantaneous_color, zorder=2.2)

    y = orbit_field_of_regard.sum() / healpix.npix * 100
    ax_time.axhspan(y, 100, color=orbit_color, zorder=2.3)

    ax_sky = fig.add_subplot(gs_sky, projection='astro hours mollweide')
    ax_sky.grid()
    ax_sky.add_artist(ax_sky.legend(
        [plt.Rectangle((0, 0), 0, 0, edgecolor='none', facecolor=color)
         for color in [orbit_color, instantaneous_color]],
        ['Orbit-averaged', 'Instantaneous'], title='Outside field of regard',
        bbox_to_anchor=[-0.05, -0.3, 1.1, 1.6], loc='upper right'))

    ax_sky.legend(
        [plt.Rectangle((0, 0), 0, 0, edgecolor=color, facecolor=color)
         for color in colors],
        survey_set,
        bbox_to_anchor=[-0.05, -0.3, 1.1, 1.6], loc='upper left')

    ax_sky.contourf_hpx(orbit_field_of_regard.astype(float), levels=[0, 0.5],
                        colors=[orbit_color], nested=nest, zorder=0.5)

    old_artists = []

    log.info('rendering animation frames')
    with tqdm(total=len(field_of_regard)) as progress:

        def animate(i):
            for artist in old_artists:
                artist.remove()
            del old_artists[:]
            for row in schedule:
                if times[i] >= row['time']:
                    poly = mission.fov.footprint(row['center']).icrs
                    idx = survey_set.index(row['survey'])
                    footprint_color = colors[idx]
                    vertices = np.column_stack((poly.ra.rad, poly.dec.rad))
                    for cut_vertices in plot.cut_prime_meridian(vertices):
                        patch = plt.Polygon(
                            np.rad2deg(cut_vertices),
                            transform=ax_sky.get_transform('world'),
                            facecolor=footprint_color,
                            edgecolor=footprint_color,
                            alpha=0.5)
                        old_artists.append(ax_sky.add_patch(patch))
            old_artists.extend(ax_sky.contourf_hpx(
                field_of_regard[i].astype(float), levels=[0, 0.5],
                colors=[instantaneous_color], nested=nest,
                zorder=0.2).collections)

            if schedule[i]['survey'] in ['kilonova', 'galactic_plane', 'GW']:
                old_artists.append(ax_sky.imshow_hpx((schedule[i]["map"],
                                                     'ICRS'),
                                                     nested=nest,
                                                     cmap='cylon'))

            old_artists.append(ax_prob.axvline(t[i], color='gray', zorder=10))
            old_artists.append(ax_time.axvline(t[i], color='gray', zorder=10))
            progress.update()

        frames = [ii for ii in range(len(field_of_regard))]
        times = times[::nslice]

        ani = FuncAnimation(fig, animate, frames=frames)
        # ani.save(args.output.name, writer=PillowWriter())
        ani.save(args.output.name, fps=30, extra_args=['-vcodec', 'libx264'])
        fig.savefig(args.output.name.replace("mp4", "pdf"))


if __name__ == '__main__':
    main()
