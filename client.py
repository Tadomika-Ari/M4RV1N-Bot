import discord
from discord.ext import commands
from json import loads
from pathlib import Path

intents = discord.Intents.default()
intents.message_content = True

config = loads(Path("config.json").read_text())

TOKEN = config["token"]

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Je suis connecté avec {bot.user}")
    await bot.change_presence(activity=discord.Game("42"), status=discord.Status.online)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$ping'):
        await message.channel.send('pong')
    
    if message.content.startswith('$invite'):
        await message.channel.send('Salut ! Mon invitation est :' '\n ''https://discord.com/oauth2/authorize?client_id=904652429381992459')
    
    if message.content.startswith('$github'):
        await message.channel.send('Salut ! Libre à toi de venir m améliorer ! voici mon lien :' '\n' 'https://github.com/Tadomika-Ari/M4RV1N-Bot')

bot.run(TOKEN)
