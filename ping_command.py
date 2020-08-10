import client

@client.client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.client.latency * 1000)}ms')
