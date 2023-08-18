from typing import Any

from discord import Activity, ActivityType, AllowedMentions, Intents, Status
from discord.ext import commands
from discord.ext.commands import HelpCommand

from bot.constants import ActivityConfig, BotConfig, Mention
from bot.log import get_logger

log = get_logger("bot")


class BotBase(commands.AutoShardedBot):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(
            BotConfig.prefix,
            activity=Activity(
                name=ActivityConfig.text,
                type=getattr(ActivityType, ActivityConfig.atype),
            ),
            allowed_mentions=AllowedMentions(
                everyone=Mention.everyone,
                users=Mention.users,
                roles=Mention.roles,
                replied_user=Mention.replied_user,
            ),
            case_insensitive=BotConfig.case_insensitive_commands,
            description=BotConfig.description,
            intents=Intents(BotConfig.intents),
            status=getattr(Status, BotConfig.status),
            help_command=HelpCommand() if BotConfig.default_help_command else None,
            **kwargs,
        )

    def run(self, *args: Any, **kwargs: Any) -> None:
        super().run(BotConfig.token, *args, **kwargs)

    async def on_ready(self) -> None:
        log.info("Bot has started!")
