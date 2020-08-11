import client

@client.client.command()
async def join(ctx, arg):
    message = ctx.message
    author = message.author
    guild_permissions = author.guild_permissions
    guild = message.guild
        

    #Adds students to the student list if not already there
    ref = client.db.reference(f'{guild.id}/Students')
    ref.child(f'{author.id}').set({
        'Student Name': f'{author.display_name}',
    })    


    #Checks if the course with the code exists and adds student if not there already
    ref = client.db.reference(f'{guild.id}/Classes/{arg}')
    
    if ref.get() is None:
        await ctx.send(f'>>> No course was found with course ID: "{arg}"')
    else:
        className = ref.get()['Class Name']
        ref = client.db.reference(f'{guild.id}/Classes/{arg}/Students')

        if ref.get() is None:
            await ctx.send(f'>>> You were added to the class: "{className}"')
        elif client.db.reference(f'{guild.id}/Classes/{arg}/Students/{author.id}').get() is None:
            await ctx.send(f'>>> You were added to the class: "{className}"')
        else:
            await ctx.send(f'>>> You are already in class: "{className}"')

        ref.child(f'{author.id}').set({
            'Student Name': f'{author.display_name}',
        })
        





    



        
    
    
