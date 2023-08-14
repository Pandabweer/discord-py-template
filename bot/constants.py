import os
from collections.abc import Generator
from pathlib import Path
from typing import Generic, TypeVar

import dotenv
import yaml

dotenv.load_dotenv()


def _env_var_constructor(loader, node) -> str | None:  # noqa: ANN001
    """
    Implements a custom YAML tag for loading optional environment
    variables. If the environment variable is set, returns the
    value of it. Otherwise, returns `None`.

    Example usage in the YAML configuration:

        # Optional app configuration. Set `MY_APP_KEY` in the environment to use it.
        application:
            key: !ENV 'MY_APP_KEY'
    """
    default = None

    # Check if the node is a plain string value
    if node.id == "scalar":
        value = loader.construct_scalar(node)
        key = str(value)
    else:
        # The node value is a list
        value = loader.construct_sequence(node)

        if len(value) >= 2:  # noqa: PLR2004
            # If we have at least two values, then we have both a key and a default value
            default = value[1]
            key = value[0]
        else:
            # Otherwise, we just have a key
            key = value[0]

    return os.getenv(key, default)


yaml.SafeLoader.add_constructor("!ENV", _env_var_constructor)

p = Path("config.yml")
with p.open(encoding="UTF-8") as f:
    _CONFIG_YAML = yaml.safe_load(f)

T = TypeVar("T")


class YAMLGetter(Generic[T], type):

    """Metaclass for getting configuration variables from the YAML file."""

    section: str
    subsection: str | None = None

    def __getattr__(cls, name: str) -> T:
        """Get a configuration variable from the YAML file."""
        name = name.lower()

        try:
            if cls.subsection is not None:
                return _CONFIG_YAML[cls.section][cls.subsection][name]
            return _CONFIG_YAML[cls.section][name]
        except KeyError as e:
            raise AttributeError(
                f"Tried accessing configuration variable {name!r} but it was nowhere to be found"
            ) from e

    def __getitem__(cls, name: str) -> T:
        """Get a configuration variable from the YAML file."""
        return cls.__getattr__(name)

    def __iter__(cls) -> Generator[tuple[str, T], None, None]:
        """Return generator of key: value pairs of current constants class' config values."""
        for name in cls.__annotations__:
            yield name, getattr(cls, name)


class BotConfig(metaclass=YAMLGetter):
    section = "bot"

    token: str
    prefix: str
    description: str
    default_help_command: bool
    debug_guild_ids: list[int]
    owner_ids: list[int]


class LoggingConfig(metaclass=YAMLGetter):
    section = "logging"

    debug: bool
    file_logs: bool
    trace_loggers: str
