import client

@client.client.command()
@client.checks.is_admin()
async def create(ctx, *, arg):
    message = ctx.message
    author = ctx.author
    
    guild = ctx.guild
    
    ref = client.db.reference(f'{guild.id}/Classes')
    class_ref = ref.push({
        'Class Name': f'{arg}',
    })    

    await ctx.send(f'>>> New class "{arg}" was added with class code: "{class_ref.key}"')
    