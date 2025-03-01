from discord import Intents
from discord.ext.commands import Bot

from application.settings import COMMAND_PREFIX

intents = Intents.all()
bot = Bot(command_prefix=COMMAND_PREFIX, intents=intents)