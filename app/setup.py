from functools import partial
from pathlib import Path

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher.filters.state import State, StatesGroup
from loguru import logger
from redis import Redis

from app import config
from app.middlewares.i18n import I18nMiddleware

app_dir: Path = Path(__file__).parent.parent
locales_dir = app_dir / "locales"

redis_factory = partial(Redis, host=config.REDIS_HOST, port=config.REDIS_PORT)
storage = RedisStorage2(
    host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB_FSM
)
stat = redis_factory(db=config.REDIS_DB_STAT)
candidate_places = redis_factory(db=config.REDIS_DB_CANDIDATE_PLACES)
selected_place = redis_factory(db=config.REDIS_DB_SELECTED_PLACE)

bot = Bot(config.TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
i18n = I18nMiddleware("bot", locales_dir, default="en")


class MainState(StatesGroup):
    location = State()


def setup():
    from app import filters, middlewares
    from app.utils import executor

    middlewares.setup(dp)
    filters.setup(dp)
    executor.setup()

    logger.info("Configure handlers...")
    import app.handlers  # noqa: F401
