import client

@client.client.command()
async def init(ctx, arg):
    guild = ctx.message.guild
    await ctx.send(f'Adding new school with server ID: {guild.id}')
