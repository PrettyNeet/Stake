import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
       await client.send_message(message.channel, 'Just hop noob')

client.run('MzE4NTAyMTg4MDM1MDgwMTky.DA0HEQ.wa9Tgwh2tSTGwiMUCs8G98UWvuE')
