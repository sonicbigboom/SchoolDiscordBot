import discord
from discord.ext import commands

def is_bot_owner():
    async def predicate(ctx):
        if ctx.author.id in ctx.bot.owner_ids:
            return True
        else:
            await ctx.send('>>> You do not own this bot!')
            return False
    
    return commands.check(predicate)

#probably will come in use idk
def is_guild_owner():
    async def predicate(ctx):
        if ctx.author.id == ctx.guild.owner.id:
            return True
        else:
            await ctx.send('>>> You are not the guild owner.')

    return commands.check(predicate)

def is_admin():
    async def predicate(ctx):
        if ctx.author.guild_permissions.administrator:
            return True
        else:
            await ctx.send('>>> You must have Administrator permissions to use this command.')
            return False

    return commands.check(predicate)

def naive_arg_check(num_args):
    #unfinished
    async def predicate(ctx):
        args = ctx.args
        print(f'Passed in {args} arguments and command takes in {num_args}')
        return True
    
    return commands.check(predicate)