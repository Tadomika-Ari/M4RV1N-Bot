import discord
from discord import bot
from json import loads
from pathlib import Path

config = loads(Path("config.json").read_text())

TOKEN = config["token"]

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

bot.run(TOKEN)
