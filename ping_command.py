import client

@client.client.command()
async def ping(ctx):
    await ctx.send(f'>>> Pong! {round(client.client.latency * 1000)}ms')

"""
@client.client.command()
async def create(ctx):
    guild = ctx.message.guild
    await guild.create_voice_channel('cool-channel')
"""