"""Configuration for the cloai module."""

import enum
import functools
import logging
from importlib import metadata
from typing import Literal

import pydantic
import pydantic_settings


def get_version() -> str:
    """Return the version of the package."""
    try:
        return metadata.version("cloai")
    except metadata.PackageNotFoundError:
        return "unknown"


class WhisperLanguages(str, enum.Enum):
    """The languages for the whisper model."""

    AFRIKAANS = "af"
    ARABIC = "ar"
    ARMENIAN = "hy"
    AZERBAIJANI = "az"
    BELARUSIAN = "be"
    BOSNIAN = "bs"
    BULGARIAN = "bg"
    CATALAN = "ca"
    CHINESE = "zh"
    CROATIAN = "hr"
    CZECH = "cs"
    DANISH = "da"
    DUTCH = "nl"
    ENGLISH = "en"
    ESTONIAN = "et"
    FINNISH = "fi"
    FRENCH = "fr"
    GALICIAN = "gl"
    GERMAN = "de"
    GREEK = "el"
    HEBREW = "he"
    HINDI = "hi"
    HUNGARIAN = "hu"
    ICELANDIC = "is"
    INDONESIAN = "id"
    ITALIAN = "it"
    JAPANESE = "ja"
    KANNADA = "kn"
    KAZAKH = "kk"
    KOREAN = "ko"
    LATVIAN = "lv"
    LITHUANIAN = "lt"
    MACEDONIAN = "mk"
    MALAY = "ms"
    MARATHI = "mr"
    MAORI = "mi"
    NEPALI = "ne"
    NORWEGIAN = "no"
    PERSIAN = "fa"
    POLISH = "pl"
    PORTUGUESE = "pt"
    ROMANIAN = "ro"
    RUSSIAN = "ru"
    SERBIAN = "sr"
    SLOVAK = "sk"
    SLOVENIAN = "sl"
    SPANISH = "es"
    SWAHILI = "sw"
    SWEDISH = "sv"
    TAGALOG = "tl"
    TAMIL = "ta"
    THAI = "th"
    TURKISH = "tr"
    UKRAINIAN = "uk"
    URDU = "ur"
    VIETNAMESE = "vi"
    WELSH = "cy"


class Settings(pydantic_settings.BaseSettings):
    """Represents the settings for the cloai module."""

    LOGGER_NAME: str = "cloai"
    LOGGER_VERBOSITY: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"

    OPENAI_API_KEY: pydantic.SecretStr | None = pydantic.Field(
        None,
        json_schema_extra={
            "env": "OPENAI_API_KEY",
            "description": "The API key for OpenAI.",
        },
    )


@functools.lru_cache
def get_settings() -> Settings:
    """Cached fetcher for the API settings.

    Returns:
        The settings for the API.
    """
    return Settings()  # type: ignore[call-arg]


def initialize_logger() -> logging.Logger:
    """Initializes the logger for the API."""
    settings = get_settings()
    logger = logging.getLogger(settings.LOGGER_NAME)
    if settings.LOGGER_VERBOSITY is not None:
        logger.setLevel(settings.LOGGER_VERBOSITY)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)s - %(funcName)s - %(message)s",  # noqa: E501
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_logger() -> logging.Logger:
    """Gets the logger for the API.

    Returns:
        The logger for the API.
    """
    settings = get_settings()
    logger = logging.getLogger(settings.LOGGER_NAME)
    if logger.hasHandlers():
        return logger
    return initialize_logger()
