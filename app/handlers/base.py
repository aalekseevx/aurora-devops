from aiogram import types
from aiogram.dispatcher.filters import CommandHelp, CommandStart
from loguru import logger

from app.formatters.messages import base as msg
from app.setup import dp


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    logger.info(
        "User {user} start conversation with bot", user=message.from_user.id
    )
    await message.answer(msg.intro(message.from_user.full_name))


@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message):
    logger.info("User {user} read help", user=message.from_user.id)
    await message.answer(msg.help())


@dp.errors_handler()
async def errors_handler(update: types.Update, exception: Exception):
    try:
        raise exception
    except Exception as e:
        logger.exception(
            "Cause exception {e} in update {update}", e=e, update=update
        )
    return True
