from bot.constants import LoggingConfig
from bot.log import get_logger

log = get_logger("bot")
log.debug(LoggingConfig.debug)
