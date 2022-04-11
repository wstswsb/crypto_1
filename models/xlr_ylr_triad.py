from typing import NamedTuple

from .xlr_ylr import XlXrYlYr


class XlXrYlYrTriad(NamedTuple):
    xl_xr_yr_yl_1: XlXrYlYr
    xl_xr_yr_yl_2: XlXrYlYr
    delta_xl_xr_yr_yl: XlXrYlYr
