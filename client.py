import asyncio
from datetime import timedelta
import discord
from discord import bot
from os import getenv
from time import *

from ressource.help import *
from ressource.smash import *

import datetime
asyncio.set_event_loop(asyncio.new_event_loop())

TOKEN = getenv("DISCORD_TOKEN")
GUILD_ID = int(getenv("GUILD_ID", "1429857134052638962"))

if not TOKEN:
    raise ValueError("DISCORD_TOKEN environment variable not set")

bot = discord.Bot()

basecommand = bot.create_group("base", "Greet people")

def time_to_timestamp(date_str):
    dt = datetime.datetime.strptime(date_str, "%d/%m/%Y")
    dt = dt.replace(tzinfo=datetime.timezone.utc)
    return int(dt.timestamp())

print(f"{time_to_timestamp("26/01/2026")}")

lol_character_list = [
    "Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe",
    "Aurelion Sol", "Azir", "Bard", "Bel'Veth", "Blitzcrank", "Brand", "Braum", "Briar", "Caitlyn",
    "Camille", "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko",
    "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen",
    "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Hwei", "Illaoi", "Irelia",
    "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "K'Sante", "Kai'Sa", "Kalista",
    "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred",
    "Kled", "Kog'Maw", "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu",
    "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Milio", "Miss Fortune", "Mordekaiser",
    "Morgana", "Naafiri", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne",
    "Nunu & Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn",
    "Rakan", "Rammus", "Rek'Sai", "Rell", "Renata Glasc", "Renekton", "Rengar", "Riven", "Rumble",
    "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed",
    "Sion", "Sivir", "Skarner", "Smolder", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench",
    "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate",
    "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vex", "Vi", "Viego", "Viktor",
    "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone",
    "Yorick", "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"
]
smash_character_list = [
    "Mario", "Donkey Kong", "Link", "Samus", "Dark Samus", "Yoshi", "Kirby", "Fox", "Pikachu",
    "Luigi", "Ness", "Captain Falcon", "Jigglypuff", "Peach", "Daisy", "Bowser", "Ice Climbers",
    "Sheik", "Zelda", "Dr. Mario", "Pichu", "Falco", "Marth", "Lucina", "Young Link", "Ganondorf",
    "Mewtwo", "Roy", "Chrom", "Mr. Game & Watch", "Meta Knight", "Pit", "Dark Pit", "Zero Suit Samus",
    "Wario", "Snake", "Ike", "Pokémon Trainer", "Diddy Kong", "Lucas", "Sonic", "King Dedede", "Olimar",
    "Lucario", "R.O.B.", "Toon Link", "Wolf", "Villager", "Mega Man", "Wii Fit Trainer", "Rosalina & Luma",
    "Little Mac", "Greninja", "Mii Brawler", "Mii Swordfighter", "Mii Gunner", "Palutena", "Pac-Man",
    "Robin", "Shulk", "Bowser Jr.", "Duck Hunt", "Ryu", "Ken", "Cloud", "Corrin", "Bayonetta", "Inkling",
    "Ridley", "Simon", "Richter", "King K. Rool", "Isabelle", "Incineroar", "Piranha Plant", "Joker",
    "Hero", "Banjo & Kazooie", "Terry", "Byleth", "Min Min", "Steve", "Sephiroth", "Pyra", "Mythra",
    "Kazuya", "Sora"
]


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
async def tableau(interaction : discord.Interaction, title: str, description: str):
   embed = discord.Embed(title=f"{title}", description=f"{description}")
   embed.add_field(name="Ceci est un test :", value=f"Ceci aussi")
   embed.set_footer(text=f"Créer par {interaction.user.name}")
   await interaction.response.send_message(embed=embed)

@bot.slash_command(name="tournoi", description="create a tournoi")
async def add_tournoi(interaction : discord.Interaction, title: str, description: str, time: str):
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
    allowed_role = ["Fondateur", "Modérateur"]
    if any(role.name in allowed_role for role in ctx.author.roles):
        await ctx.respond("test !")
    else:
        await ctx.respond("Tu n’as pas le rôle requis.", ephemeral=True)

@bot.slash_command(name="purge", description="Clear un salon pour le rendre clean", guild_ids=[GUILD_ID])
async def purge(ctx: discord.ApplicationContext, nb_message: int):
   allowed_role = ["Fondateur", "Modérateur"]
   print("Commande Purge")
   embed = discord.Embed(title="PURGE !", description="Purge terminé")
   embed.set_image(url="https://images-ext-1.discordapp.net/external/HiaeokP0KFI8PXVeq_SpiMNZ9-Qe0cQsQWicSn35PGo/https/media.tenor.com/FwNuvPzK6IIAAAPo/nuke-it-olliesblog-olliesblog-nuke-it.mp4")
   if any(role.name in allowed_role for role in ctx.author.roles):
      if (nb_message < 1):
            await ctx.respond("nb de message pas assez", ephemeral=True)
            return
      if (nb_message > 100):
            await ctx.respond("nb de message au dessus de 100", ephemeral=True)
            return
      await ctx.respond("Purge en cours...", ephemeral=True)
      messages = [message async for message in ctx.channel.history(limit=nb_message)]
      now = discord.utils.utcnow()
      recent = [m for m in messages if (now - m.created_at) < timedelta(days=14)]
      old = [m for m in messages if m not in recent]
      if recent:
        await ctx.channel.delete_messages(recent)
      for message in old:
        await message.delete()
      await ctx.followup.send(embed=embed)
      sleep(5)
      await ctx.channel.purge(limit=1)
   else:
      await ctx.respond("Tu n’as pas le rôle requis.", ephemeral=True)

@bot.slash_command(name="banlist", description="Choisie le jeu et le nombre, je m'occupe du reste")
async def tabban(interaction : discord.Interaction, name : str, nb: int):
  print("ok1")
  match (name):
      case "smash":
        list = random_ban_character(smash_character_list, nb)
      case "lol":
        list = random_ban_character(lol_character_list, nb)
      case _:
        list = []
  
  embed = discord.Embed(title=f"La ban list de Smash", description="La list de ban pour cette partie est la suivante : ")
  embed.add_field(name=name, value=list)
  await interaction.response.send_message(embed=embed)

@bot.slash_command(name="admin_only", description="Commande réservée aux admins")
async def admin_only(ctx):
    if "Fondateur" in [role.name for role in ctx.author.roles]:
        await ctx.respond("Commande admin exécutée !")
    else:
        await ctx.respond("Tu n’as pas le rôle requis.", ephemeral=True)

@bot.slash_command(name="pokepitech", description="Info pour pokepitech", guild_ids=[GUILD_ID])
async def pokepitech(interaction : discord.Interaction):
   print("Commande pokepitech")
   embed = discord.Embed(title=f"Info pour le serveur MC Pokepitech", description="Le serveur est ouvert 24h/24\n " \
   "C'est un serveur Minecraft moddé basé sur le modpack Cobblemon\n")
   embed.add_field(name="Comment Rejoindre ?", value="Pour y accéder, il vous faut installer le modpack via forge !" \
   "Il vous faut donc installer CursForge via ce [lien](https://www.curseforge.com/download/app)\n" \
   "\n" \
   "Puis installer le modpack CurseForge : https://www.curseforge.com/minecraft/modpacks/cobblemon-academy-2-0/\n" \
   "ET VOILA ! Vous pouvez accéder au serveur via cette IP : srv1296100.hstgr.cloud:25565\n")
   embed.set_footer(text="Mise en place par les membres du club EpiGaming")
   await interaction.response.send_message(embed=embed)

@bot.slash_command(name="episerv", description="Info pour l'Episerv", guild_ids=[GUILD_ID])
async def pokepitech(interaction : discord.Interaction):
   print("Commande Episerv")
   embed = discord.Embed(title=f"Info pour le serveur MC Episerv !", description="Le serveur n'est pas encore ouvert\n " \
   "C'est un serveur Minecraft moddé basé sur un modpack fait maison\n")
   embed.add_field(name="Comment Rejoindre ?", value="Pour y accéder, il vous faut installer le modpack via forge !" \
   "Il vous faut donc installer CursForge via ce [lien](https://www.curseforge.com/download/app)\n" \
   "\n" \
   "Puis installer le modpack CurseForge : Pas encore\n" \
   "ET VOILA ! Vous pouvez accéder au serveur via cette IP : Pas encore\n")
   await interaction.response.send_message(embed=embed)


@bot.slash_command(name="help", description="The help function")
async def help(interaction : discord.Interaction):
  print("Commande help")
  embed = discord.Embed(title=f"This is the /help command", description=my_help())
  await interaction.response.send_message(embed=embed)

@bot.slash_command(name="mod_installation", description="Info pour installer un mod", guild_ids=[GUILD_ID])
async def tuto_mod(interaction : discord.Interaction):
   print("Commande tuto_mod")
   embed = discord.Embed(
    title="Tutoriel : Comment installer un mod",
    description=(
        "Installer des mods peut sembler compliqué au début, mais en réalité c’est assez simple une fois que l’on connaît les bonnes étapes.\n\n"
        "Avant de commencer, vous devez :\n"
        "• Choisir la **version du jeu** compatible avec le mod\n"
        "• Choisir le **type de mod loader** (exemples : Forge, Fabric, NeoForge)\n"))
   embed.add_field(
    name="Comment installer un mod ?",
    value=(
        "**Méthode recommandée (la plus simple)**\n"
        "Utilisez une application tierce comme :\n"
        "• CurseForge : https://www.curseforge.com/download/app\n"
        "• Modrinth : https://modrinth.com/app\n\n"
        "**Étapes avec Modrinth / CurseForge**\n"
        "1. Lancez l'application\n"
        "2. Cliquez sur le bouton **[ + ]** pour créer une nouvelle instance / modpack\n"
        "3. Choisissez la version du jeu et le mod loader souhaité\n\n"
        "**Ajouter des mods**\n"
        "• Si vous avez déjà un modpack, vous pouvez sauter l’étape précédente\n"
        "• Ouvrez votre modpack\n"
        "• Cliquez sur **[ + Add content ]** ou **[ Browse content ]**\n"
        "• Recherchez les mods que vous souhaitez installer\n"
        "• Cliquez sur **Installer**\n\n"
        "Et voilà ! Vos mods sont prêts à être utilisés.\n\n"
        "**Conseils utiles** :\n"
        "• Vérifiez toujours la compatibilité des mods entre eux\n"
        "• Assurez-vous que tous les mods utilisent le même mod loader\n"
        "• Évitez de mélanger Forge et Fabric dans un même modpack\n"),inline=False)
   embed.set_footer(text="Guide fait par Alessandro P.")
   await interaction.response.send_message(embed=embed)


bot.run(TOKEN)
