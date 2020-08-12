import client

@client.client.command()
@client.checks.is_admin()
async def create(ctx, *, arg):
    message = ctx.message
    author = ctx.author
    
    guild = ctx.guild
    
    #Adds students to the student list if not already there
    ref = client.db.reference(f'{guild.id}/Teachers')
    ref.child(f'{author.id}').set({
        'Teacher Name': f'{author.display_name}',
    }) 

    ref = client.db.reference(f'{guild.id}/Classes')
    class_ref = ref.push({
        'Class Name': f'{arg}',
        'Teacher': f'{author.id}'
    })    

    await ctx.send(f'>>> New class "{arg}" was added with class code: "{class_ref.key}"')
    