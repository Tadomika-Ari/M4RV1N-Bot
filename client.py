import discord
from discord import bot
from json import loads
from pathlib import Path

from ressource.help import *

config = loads(Path("config.json").read_text())

TOKEN = config["token"]

bot = discord.Bot()

basecommand = bot.create_group("base", "Greet people")

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    print("Commande Hello")
    await ctx.respond("Hey!")

@basecommand.command()
async def bye(ctx):
  print("Commande Bye")
  await ctx.respond(f"Bye, {ctx.author}!")

@basecommand.command(name="ping", description="Say hello to the bot")
async def ping(ctx):
   print("Commande Ping")
   await ctx.respond(f"Pong ! {bot.latency} ms")

@bot.slash_command(name="embed", description="Create a embed")
async def tableau(interaction : discord.Interaction, title: str, description: str, time: str):
   embed = discord.Embed(title=f"{title}", description=f"{description}")
   embed.add_field(name="Le tournoi commence dans :", value=f"Le trournoi commance dans <t:{time}:R>")
   embed.set_footer(text=f"Créer par {interaction.user.name}")
   await interaction.response.send_message(embed=embed)
   
@bot.slash_command(name="bio", description="The bio of Marvin")
async def bio(ctx):
  print("Commande bio")
  await ctx.respond(f"Je suis Marvin, un robot de l'univers de H2G2. J'ai été développé afin de subvenir aux besoins du serveur Club Epigaming. Maintenant que je suis là l'avenir de ce serveur est sauvé!")

@bot.slash_command(name="ban", description="its a ban !")
async def ban(ctx: discord.ApplicationContext):
    if ctx.author.guild_permissions.ban_members:
      print("its a test")
    else:
       print("pas la perm")

@bot.slash_command(name="help", description="The help function")
async def help(interaction : discord.Interaction):
  print("Commande help")
  embed = discord.Embed(title=f"This is the /help command", description=my_help())
  await interaction.response.send_message(embed=embed)


bot.run(TOKEN)
