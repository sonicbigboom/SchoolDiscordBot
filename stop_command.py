import client
from sys import exit

@client.client.command()
@client.checks.is_bot_owner()
async def stop(ctx):
    await ctx.send('>>> School is over.') #lol
    await client.client.close()

    exit()