import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready(): 
    print('Bot is ready.')

client.run('NzQyNDM5NjcxNTI2NTg4NTE5.XzGI0w.cTSOPpT_InZZZ7s4dA7l1UPigJc')