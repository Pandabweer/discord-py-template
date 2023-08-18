import asyncio
import os
from typing import TYPE_CHECKING

from bot import log

if TYPE_CHECKING:
    from bot.bot import BotBase

log.setup()

# On Windows, the selector event loop is required for aiodns.
if os.name == "nt":
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy(),  # type: ignore[attr-defined]
    )

instance: "BotBase" = None  #  type: ignore[assignment]
