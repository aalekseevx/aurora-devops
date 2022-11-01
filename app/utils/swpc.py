from datetime import datetime
from typing import Tuple

import requests
from loguru import logger

from app import misc

IndicesRow = Tuple[int, float, float, float, float, float, float]


def get_kp_index():
    def handle_row(row: IndicesRow):
        return datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S"), float(row[1])

    try:
        response = requests.get(misc.SWPC_1_MINUTE_KP_INDEX)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        logger.exception("Error while downloading/parsing kp index.")
        return None
    return handle_row(data[-1])
