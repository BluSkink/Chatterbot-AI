import logging
import discord
from discord.ext import commands
from bot.training import create_chatbot, train_bot
from bot.config import DISCORD_BOT_TOKEN, COMMAND_PREFIX

# Set up logging
logging.basicConfig(filename="bot_logs.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

intents = discord.Intents.default()
intents.messages = True
bot_client = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

chatbot = create_chatbot()
train_bot(chatbot)

@bot_client.event
async def on_ready():
    print(f"✅ Logged in as {bot_client.user}")

@bot_client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot_client.event
async def on_message(message):
    if message.author.bot:
        return

    response = chatbot.get_response(message.content)
    
    # Log if response confidence is too low or if the response is bad
    if response.confidence < 0.5:  # Confidence threshold can be adjusted
        logging.info(f"Bad response to '{message.content}': {response}")
    
    await message.channel.send(str(response))
    await bot_client.process_commands(message)

bot_client.run(DISCORD_BOT_TOKEN)
