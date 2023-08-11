from typing import ClassVar

from pydantic_settings import BaseSettings


class EnvConfig(
    BaseSettings,  #  type: ignore[misc]
    env_file=(".env.server", ".env"),
    env_file_encoding="utf-8",
    env_nested_delimiter="__",
    extra="ignore",
):  # type: ignore[call-arg]

    """Our default configuration for models that should load from .env files."""


class _Miscellaneous(EnvConfig):
    debug: ClassVar[bool] = True
    file_logs: ClassVar[bool] = False


Miscellaneous = _Miscellaneous()


FILE_LOGS = Miscellaneous.file_logs
DEBUG_MODE = Miscellaneous.debug


class _Bot(EnvConfig, env_prefix="bot_"):  # type: ignore[call-arg]
    token: ClassVar[str] = ""
    trace_loggers: ClassVar[str] = "*"
    debug_guild_id: ClassVar[list[int]] = []
    owner_ids: ClassVar[list[int]] = []


Bot = _Bot()
