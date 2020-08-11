import client

@client.client.command()
async def create(ctx, *, arg):
    message = ctx.message
    author = message.author
    guild_permissions = author.guild_permissions

    if guild_permissions.administrator:
        guild = message.guild
        
        ref = client.db.reference(f'{guild.id}/Classes')
        class_ref = ref.push({
            'Class Name': f'{arg}',
        })    

        await ctx.send(f'>>> New class "{arg}" was added with class code: "{class_ref.key}"')
    else:
        await ctx.send(f'>>> You must have Administrator permissions to use this command.')


        
    
    
