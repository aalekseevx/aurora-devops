from app.setup import i18n

_ = i18n.gettext


def intro(username: str) -> str:
    return _(
        "Hello, {user}.\n"
        "Send me your location to finish configuration. "
        "Alternatively, you can text me the location you are interested."
    ).format(user=username)


def help() -> str:
    return "\n".join(
        [
            _("Here you can read the list of my commands:"),
            _("{command} - Start conversation with bot").format(
                command="/start"
            ),
            _("{command} - Get this message").format(command="/help"),
            _("Articles"),
            _("News of the bot: @alekseev_wall"),
            _("Question on the project @aalekseevx"),
            _("Credentials"),
            _("Patreon"),
        ]
    )
