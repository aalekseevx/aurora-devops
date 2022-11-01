import requests

from app import misc


def get_weather_data(latitude: float, longitude: float):
    return requests.get(
        url=misc.OPEN_WEATHER_URL,
        params={
            "lat": latitude,
            "lon": longitude,
            "appid": misc.OPEN_WEATHER_TOKEN,
        },
    ).json()
