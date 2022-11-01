from app.setup import i18n

_ = i18n.gettext


def choose_kp() -> str:
    return _("Choose KP")


def choose_kp_success(kp: int) -> str:
    return _("Success {kp}").format(kp=kp)
