import os
from dotenv import load_dotenv

load_dotenv()

# Bot settings
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
COMMAND_PREFIX = "!"
