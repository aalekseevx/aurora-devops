from aiogram import Dispatcher
from loguru import logger


def setup(dispatcher: Dispatcher):
    logger.info("Configure filters...")
    from .superuser import IsSuperuserFilter

    text_messages = [  # noqa: F841
        dispatcher.message_handlers,
        dispatcher.edited_message_handlers,
        dispatcher.channel_post_handlers,
        dispatcher.edited_channel_post_handlers,
    ]

    dispatcher.filters_factory.bind(IsSuperuserFilter)
