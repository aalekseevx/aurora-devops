from dataclasses import dataclass, field
from typing import Any, Tuple

from aiogram.contrib.middlewares.i18n import I18nMiddleware as BaseI18nMiddleware  # noqa: E501
from aiogram.utils.emoji import emojize


@dataclass
class LanguageData:
    flag: str
    title: str
    label: str = field(init=False, default=None)

    def __post_init__(self):
        self.label = f"{self.flag} {self.title}"


class I18nMiddleware(BaseI18nMiddleware):
    AVAILABLE_LANGUAGES = {
        "en": LanguageData(emojize(":United_Kingdom:"), "English"),
        "ru": LanguageData(emojize(":Russia:"), "Русский"),
    }

    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        data: dict = args[-1]
        if "chat" in data:
            return data["chat"].language or self.default
        return self.default
