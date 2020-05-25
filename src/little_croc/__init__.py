# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound
from pathlib import Path

here = Path(__file__).parent

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = 'little-croc'
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound
