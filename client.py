import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

TOKEN = "OTA0NjUyNDI5MzgxOTkyNDU5.GL3HVI.leK9T75H-q7UcBaFGU12oZpvKr7wmbwNSoUvAI"

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Je suis connecté")
    await bot.change_presence(activity=discord.Game("Test"), status=discord.Status.online)



bot.run(TOKEN)