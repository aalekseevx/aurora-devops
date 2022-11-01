import datetime as dt
from typing import Union

import aacgmv2

from app import misc


def get_desired_kp(latitude: float, longitude: float) -> Union[int, None]:
    magnetic_latitude = aacgmv2.get_aacgm_coord(
        latitude, longitude, 0, dt.datetime.now()
    )[0]
    desired_kp = min(
        [
            (abs(magnetic_latitude - desired_latitude), kp)
            for kp, desired_latitude in misc.DESIRED_MAGNETIC_LATITUDE.items()
        ]
    )[1]
    if (
        desired_kp == 9
        and magnetic_latitude < misc.DESIRED_MAGNETIC_LATITUDE[desired_kp]
    ):
        return None
    return desired_kp
