from discord import Intents
from discord.ext import commands
from discord.ext.commands import HelpCommand

from bot.constants import BotConfig


class BotBase(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            command_prefix=BotConfig.prefix,
            description=BotConfig.description,
            intents=Intents(BotConfig.intents),
            help_command=HelpCommand() if BotConfig.default_help_command else None,
            **kwargs,
        )

    async def run(self, *args, **kwargs) -> None:
        super().run(BotConfig.token, *args, **kwargs)
