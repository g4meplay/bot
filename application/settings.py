import logging
import logging.config
from os import getenv as env
from dotenv import load_dotenv as load
from pathlib import Path
from nextcord import Intents

# Diretório raiz do projeto
BASE_DIR = Path(__file__).parent.parent

# Carrega as variáveis de ambiente
load(BASE_DIR / ".env", override=True)
load(BASE_DIR / ".env.example", override=False)

# Token do bot do Discord
TOKEN = env("TOKEN")

# Prefixo de comando do bot
COMMAND_PREFIX = env("COMMAND_PREFIX")

# Permissões
INTENTS = Intents.all()

EXTENSIONS = [
    "common.events"
]
