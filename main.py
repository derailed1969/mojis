import discord
import os
from collections import defaultdict

client = discord.Client()
forgor = '💀'
token = os.environ['TOKEN']
allowedG = {}
sorry = "sorry i didn't mean to make you mad"
words = ['forgot', 'forget']

@client.event
async def on_ready():
  print("hi")

@client.event
async def on_message(message):
  tempID = message.channel.guild.id
  try:
    if allowedG[tempID] == 1:
      if message.content.startswith('shut the fuck up you stupid cunt'):
        allowedG[tempID] = 0
        await message.channel.send("sohrry i didn;tt me an to make oyyu ma,;d")
      if "forgor" in message.content.lower() and not message.author == client.user:
        await message.add_reaction(forgor)
      if any(checkW in message.content.lower() for checkW in words):
        await message.channel.send("* forgor")
    else:
      if message.content.startswith('i love you mojis'):
        allowedG[tempID] = 1
        await message.channel.send("ok")
  except KeyError:
    if message.content.startswith('i love you mojis'):
        allowedG[tempID] = 1
        await message.channel.send("ok")
client.run(token)