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
    file_logs: ClassVar[bool] = True


Miscellaneous = _Miscellaneous()


FILE_LOGS = Miscellaneous.file_logs
DEBUG_MODE = Miscellaneous.debug


class _Bot(EnvConfig, env_prefix="bot_"):  # type: ignore[call-arg]
    token: ClassVar[str] = ""
    trace_loggers: ClassVar[str] = "*"
    default_enabled_guilds: ClassVar[list[int]] = [934896901256515714]
    owner_ids: ClassVar[list[int]] = [169790484594556928]


Bot = _Bot()
