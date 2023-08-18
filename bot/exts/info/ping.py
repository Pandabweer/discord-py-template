from discord import Interaction
from discord.app_commands import command
from discord.ext.commands import Cog

from bot.bot import BotBase
from bot.log import get_logger

log = get_logger(__name__)


class Ping(Cog):
    def __init__(self, bot: BotBase) -> None:
        self.bot = bot

    @command(name="ping")
    async def ping(self, interaction: Interaction) -> None:
        await interaction.response.send_message("Hello world!")


async def setup(bot: BotBase) -> None:
    await bot.add_cog(Ping(bot))
