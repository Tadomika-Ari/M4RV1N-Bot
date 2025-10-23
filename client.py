import discord
from discord.ext import commands
from json import loads
from pathlib import Path

intents = discord.Intents.default()
intents.message_content = True

config = loads(Path("config.json").read_text())

TOKEN = config["token"]

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Je suis connecté")
    await bot.change_presence(activity=discord.Game("42"), status=discord.Status.online)



bot.run(TOKEN)
