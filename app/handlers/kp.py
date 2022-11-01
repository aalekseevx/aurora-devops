from aiogram import types
from aiogram.dispatcher.filters.filters import OrFilter

from app.formatters.markup import kp as markup
from app.formatters.messages import kp as msg
from app.models.chat import Chat
from app.setup import dp


@dp.message_handler(commands="kp")
async def cmd_kp(message: types.Message):
    await message.answer(msg.choose_kp(), reply_markup=markup.choose_kp())


@dp.callback_query_handler(OrFilter(*[f"kp_{i}".__eq__ for i in range(0, 10)]))
async def kp_callback(call: types.CallbackQuery, chat: Chat):
    kp = int(call.data[len("kp_") :])
    await chat.update(desired_kp=kp).apply()
    await call.message.edit_text(msg.choose_kp_success(kp), reply_markup=None)
    await call.answer()
