import discord
from discord.ext import commands

import config

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready(): 
    print('Bot is ready.')

client.run(config.TOKEN)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
