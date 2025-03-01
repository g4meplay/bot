from application.settings import COMMAND_PREFIX as command_prefix
from application.settings import EXTENSIONS as extensions
from application.settings import INTENTS as intents

from nextcord.ext.commands import Bot

bot = Bot(
    command_prefix=command_prefix, 
    intents=intents
)

bot.load_extensions(extensions)
