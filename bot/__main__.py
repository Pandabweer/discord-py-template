import bot
from bot.bot import BotBase

bot.instance = BotBase()
bot.instance.run(log_handler=None)
