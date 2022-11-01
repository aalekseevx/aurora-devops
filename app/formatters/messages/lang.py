from app.setup import i18n

_ = i18n.gettext


def choose_lang() -> str:
    return _("Choose language")


def lang_changed() -> str:
    return _("Language changed to English")
