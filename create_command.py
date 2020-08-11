import client

@client.client.command()
async def create(ctx, *, arg):
    message = ctx.message
    author = message.author
    guild_permissions = author.guild_permissions

    if guild_permissions.administrator:
        guild = message.guild
        
        ref = client.db.reference(f'{guild.id}/Classes')
        ref.push({
            'Class Code': {
                'Class Name': f'{arg}'
            },
        })        


    else:
        await ctx.send(f'>>> You must have Administrator permissions to use this command.')


        
    
    
