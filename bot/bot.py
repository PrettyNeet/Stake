import discord
import asyncio
import youtube_dl
from discord.ext import commands

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def hop():
    await client.send_message('just hop noob')

@client.event
async def on_message(message):
    if message.content.startswith('!shanty'):
        await client.send_message(message.channel, 'Sea Shanty Time!')
        channel = message.author.voice_channel
        voice = await client.join_voice_channel(channel)
        player = await voice.create_ytdl_player('https://youtu.be/RH5rEvxFLvM')
        player.start()

@client.event
async def on_message(message):
    if message.content.startswith('!leave'):
        await player.stop()
        try:
            await player.disconnect()
        except:
            pass

client.run('token')
