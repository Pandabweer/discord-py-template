from typing import Any

from discord import Intents
from discord.ext import commands
from discord.ext.commands import HelpCommand

from bot.constants import BotConfig


class BotBase(commands.Bot):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(
            BotConfig.prefix,
            description=BotConfig.description,
            intents=Intents(BotConfig.intents),
            help_command=HelpCommand() if BotConfig.default_help_command else None,
            **kwargs,
        )

    def run(self, *args: Any, **kwargs: Any) -> None:
        super().run(BotConfig.token, *args, **kwargs)
