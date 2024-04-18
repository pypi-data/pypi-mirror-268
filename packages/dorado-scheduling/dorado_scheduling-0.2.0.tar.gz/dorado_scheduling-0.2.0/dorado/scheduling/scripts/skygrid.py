#
# Copyright © 2021 United States Government as represented by the Administrator
# of the National Aeronautics and Space Administration. No copyright is claimed
# in the United States under Title 17, U.S. Code. All Other Rights Reserved.
#
# SPDX-License-Identifier: NASA-1.3
#
"""Generate a grid of pointings on the sky."""
import astropy.units as u
from astropy.table import QTable
import numpy as np

from ligo.skymap.tool import ArgumentParser, FileType

from .. import skygrid


def parser():
    p = ArgumentParser(prog='dorado-scheduling-skygrid')
    p.add_argument('--area', default='50 deg2', type=u.Quantity,
                   help='Average area per tile')
    p.add_argument('--method', default='healpix', help='Tiling algorithm',
                   choices=[key.replace('_', '-') for key in skygrid.__all__])
    p.add_argument('-o', '--output', metavar='OUTPUT.ecsv', default='-',
                   type=FileType('w'), help='Output filename')
    return p


def main(args=None):
    args = parser().parse_args(args)

    method = getattr(skygrid, args.method.replace('-', '_'))
    coords = method(args.area)
    table = QTable({'field_id': np.arange(len(coords)), 'center': coords})
    table.write(args.output, format='ascii.ecsv')


if __name__ == '__main__':
    main()
