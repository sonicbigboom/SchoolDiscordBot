import client

@client.client.command()
async def init(ctx, arg):
    guild = ctx.message.guild
    ref = client.db.reference(f'{guild.id}')

    if ref.get() is None:
        ref = client.db.reference('/')
        ref.set({
            f'{guild.id}': 
                {
                    'Name': f'{arg}'
                }   
        })
        await ctx.send(f'```Adding new school {arg} with server ID: {guild.id}```')
    else:
        await ctx.send(f'```School with this server id already exists!```')
        
    
    
