from app.setup import i18n

_ = i18n.gettext


def enter_location() -> str:
    return _("Enter location")


def settings_updated(
    latitude: float, longitude: float, geonames_data: dict, desired_kp: int
) -> str:
    return "\n".join(
        [
            _("Settings updated:"),
            _("Coordinates: {latitude}, {longitude}").format(
                latitude=latitude, longitude=longitude
            ),
            _("Timezone: {timezone}").format(
                timezone=geonames_data["timezoneId"]
            ),
            _("Desired kp: {desired_kp}".format(desired_kp=desired_kp)),
        ]
    )


def choose_location(place: dict) -> str:
    return _("{name}, {country}\n ({latitude}, {longitude})").format(
        name=place["name"],
        country=place["countryName"],
        latitude=place["lat"],
        longitude=place["lng"],
    )


def places_not_found() -> str:
    return _("Places not found")
