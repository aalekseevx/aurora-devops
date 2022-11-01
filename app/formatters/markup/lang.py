from aiogram import types

from app.handlers.lang import cb_chat_settings
from app.setup import i18n


def choose_lang() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    for code, language in i18n.AVAILABLE_LANGUAGES.items():
        markup.add(
            types.InlineKeyboardButton(
                language.label,
                callback_data=cb_chat_settings.new(
                    property="language", value=code
                ),
            )
        )
    return markup
