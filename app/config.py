import secrets

from envparse import env

TELEGRAM_TOKEN = env.str("TELEGRAM_TOKEN", default="-")
BOT_PUBLIC_PORT = env.int("BOT_PUBLIC_PORT", default=8080)

DOMAIN = env.str("DOMAIN", default="example.com")
SECRET_KEY = secrets.token_urlsafe(48)
WEBHOOK_BASE_PATH = env.str("WEBHOOK_BASE_PATH", default="/webhook")
WEBHOOK_HTTPS = env.bool("WEBHOOK_HTTPS", default=True)
WEBHOOK_PATH = f"{WEBHOOK_BASE_PATH}/{SECRET_KEY}"
WEBHOOK_URL = f"http{'s' if WEBHOOK_HTTPS else ''}://{DOMAIN}{WEBHOOK_PATH}"

REDIS_HOST = env.str("REDIS_HOST", default="localhost")
REDIS_PORT = env.int("REDIS_PORT", default=6379)
REDIS_DB_FSM = env.int("REDIS_DB_FSM", default=0)
REDIS_DB_JOBSTORE = env.int("REDIS_DB_JOBSTORE", default=1)
REDIS_DB_JOIN_LIST = env.int("REDIS_DB_JOIN_LIST", default=2)
REDIS_DB_STAT = env.int("REDIS_DB_STAT", default=3)
REDIS_DB_CANDIDATE_PLACES = env.int("REDIS_DB_CANDIDATE_PLACES", default=4)
REDIS_DB_SELECTED_PLACE = env.int("REDIS_DB_CANDIDATE_PLACES", default=5)

POSTGRES_HOST = env.str("POSTGRES_HOST", default="localhost")
POSTGRES_PORT = env.int("POSTGRES_PORT", default=5432)
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD", default="password")
POSTGRES_USER = env.str("POSTGRES_USER", default="aiogram")
POSTGRES_DB = env.str("POSTGRES_DB", default="aiogram")
POSTGRES_URI = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

SUPERUSER_STARTUP_NOTIFIER = env.bool(
    "SUPERUSER_STARTUP_NOTIFIER", default=True
)
