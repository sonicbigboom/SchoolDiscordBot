import client

@client.client.command()
@client.checks.is_admin()
async def init(ctx, *, arg):
    message = ctx.message
    author = ctx.author

    guild = ctx.guild
    ref = client.db.reference(f'{guild.id}')

    if not ref.get():
        ref = client.db.reference('/')
        ref.set({
            f'{guild.id}': 
                {
                    'Name': f'{arg}',
                    'Classes': '{}'
                }   
        })
        await ctx.send(f'>>> Adding new school {arg} with server ID: {guild.id}')
    else:
        await ctx.send(f'>>> School with this server id already exists!')

  
