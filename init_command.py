import client

@client.client.command()
async def init(ctx, *, arg):
    message = ctx.message
    author = message.author
    guild_permissions = author.guild_permissions

    if guild_permissions.administrator:
        guild = message.guild
        ref = client.db.reference(f'{guild.id}')

        if ref.get() is None:
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
    else:
        await ctx.send(f'>>> You must have Administrator permissions to use this command.')


        
    
    
