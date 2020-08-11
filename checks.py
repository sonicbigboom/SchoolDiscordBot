import discord
from discord.ext import commands

def is_admin():
    async def predicate(ctx):
        if ctx.author.guild_permissions == guild_permissions.administrator:
            return True
        else:
            await ctx.send('>>> You must have Administrator permissions to use this command.')
            return False

    return commands.check(predicate)

