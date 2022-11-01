from datetime import timedelta

GEONAMES_USERNAME = "aurora_bot"
GEONAMES_TIMEZONE_URL = "http://api.geonames.org/timezoneJSON"
GEONAMES_SEARCH_URL = "http://api.geonames.org/searchJSON"

MAX_PLACES_SUGGESTIONS = 100

OPEN_WEATHER_TOKEN = "919cab55d431c8f969bf04bcb6160490"
OPEN_WEATHER_URL = "https://api.openweathermap.org/data/2.5/forecast"

SWPC_GEOMAGNETIC_INDICES_URL = "https://services.swpc.noaa.gov/experimental/products/geospace/geomagnetic-indices.json"  # noqa: E501
SWPC_1_MINUTE_KP_INDEX = "https://services.swpc.noaa.gov/products/noaa-estimated-planetary-k-index-1-minute.json"  # noqa: E501
SWPC_AURORA_NOWCAST_URL = "https://services.swpc.noaa.gov/text/aurora-nowcast-hemi-power.txt"  # noqa: E501
SWPC_3DAY_FORECAST_URL = (
    "https://services.swpc.noaa.gov/text/3-day-forecast.txt"  # noqa: E501
)
SWPC_27DAY_FORECAST_URL = (
    "https://services.swpc.noaa.gov/text/27-day-outlook.txt"  # noqa: E501
)
SWPC_DISCUSSION_URL = (
    "https://services.swpc.noaa.gov/text/discussion.txt"  # noqa: E501
)

DESIRED_MAGNETIC_LATITUDE = {
    0: 66.5,
    1: 64.5,
    2: 62.4,
    3: 60.4,
    4: 58.3,
    5: 56.3,
    6: 54.2,
    7: 52.2,
    8: 50.1,
    9: 48.1,
}

DIGITS_EMOJI = [
    ":zero:",
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:",
    ":seven:",
    ":eight:",
    ":nine:",
]

from app.setup import i18n  # noqa: E402

_ = i18n.gettext

DURATION_PRESETS = {
    timedelta(days=1): _("1 day"),
    timedelta(days=3): _("3 days"),
    timedelta(days=7): _("1 week"),
    timedelta(weeks=5000): _("forever"),
}
