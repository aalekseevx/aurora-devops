from aiogram import types
from aiogram.utils.emoji import emojize


def choose_location(i: int, length: int) -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    first_row = []
    if i > 0:
        first_row.append(
            types.InlineKeyboardButton(
                emojize(":arrow_backward:"), callback_data="prev"
            )
        )
    if i < length - 1:
        first_row.append(
            types.InlineKeyboardButton(
                emojize(":arrow_forward:"), callback_data="next"
            )
        )
    markup.row(*first_row)
    markup.row(
        types.InlineKeyboardButton(
            emojize(":white_check_mark:"), callback_data="ok"
        ),
        types.InlineKeyboardButton(emojize(":x:"), callback_data="cancel"),
    )
    return markup


def enter_location() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(emojize(":x:"), callback_data="cancel")
    )
    return markup
