import requests

from app import misc


def get_geonames_data(latitude: float, longitude: float):
    return requests.get(
        url=misc.GEONAMES_TIMEZONE_URL,
        params={
            "lat": latitude,
            "lng": longitude,
            "username": misc.GEONAMES_USERNAME,
        },
    ).json()


def get_place_suggestions(place: str, lang: str):
    return requests.get(
        url=misc.GEONAMES_SEARCH_URL,
        params={
            "q": place,
            "maxRows": misc.MAX_PLACES_SUGGESTIONS,
            "lang": lang,
            "username": misc.GEONAMES_USERNAME,
        },
    ).json()["geonames"]
