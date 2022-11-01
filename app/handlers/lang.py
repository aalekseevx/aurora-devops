from aiogram import types
from aiogram.dispatcher.filters.filters import OrFilter
from aiogram.utils.callback_data import CallbackData
from loguru import logger

from app.models.chat import Chat
from app.setup import dp, i18n

cb_chat_settings = CallbackData("chat", "property", "value")

from app.formatters.markup import lang as markup  # noqa: E402
from app.formatters.messages import lang as msg  # noqa: E402


@dp.message_handler(commands="lang")
async def cmd_lang(message: types.Message):
    await message.answer(
        msg.choose_lang(),
        reply_markup=markup.choose_lang(),
    )


@dp.callback_query_handler(
    OrFilter(
        *[
            cb_chat_settings.filter(property="language", value=code)
            for code in i18n.AVAILABLE_LANGUAGES
        ]
    )
)
async def cq_lang(query: types.CallbackQuery, chat: Chat, callback_data: dict):
    target_language = callback_data["value"]
    logger.info(
        "User {user} set language in chat {chat} to {language}",
        user=query.from_user.id,
        chat=chat.id,
        language=target_language,
    )

    i18n.ctx_locale.set(target_language)
    await chat.update(language=target_language).apply()
    await query.message.edit_text(msg.lang_changed(), reply_markup=None)
