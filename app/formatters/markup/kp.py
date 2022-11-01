from aiogram import types
from aiogram.utils.emoji import emojize

from app import misc


def choose_kp() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            emojize(misc.DIGITS_EMOJI[0]), callback_data=f"kp_{0}"
        )
    )
    markup.add(
        *[
            types.InlineKeyboardButton(
                emojize(digit), callback_data=f"kp_{i + 1}"
            )
            for i, digit in enumerate(misc.DIGITS_EMOJI[1:])
        ]
    )
    return markup
