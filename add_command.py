import client

@client.client.command()
@client.checks.is_admin()
async def add(ctx, code, day, start, end):
    message = ctx.message
    author = ctx.author
    guild = ctx.guild
    
    ref = client.db.reference(f'{guild.id}/Classes/{code}')
    
    if ref.get() is not None:
        ref = client.db.reference(f'{guild.id}/Classes/{code}/Blocks')
        if ref.get() is not None:
            ref = client.db.reference(f'{guild.id}/Classes/{code}/Blocks/{day.lower()} {start}')
            if ref.get() is not None:
                await ctx.send(f'>>> This class already has a meet set up at this time')
            else:
                #Adds meet to blocks
                ref.child(f'{day.lower()} {start}').set({
                    'Start': f'{start}',
                    'End': f'{end}'
                })

                #Adds class to meets
                ref = client.db.reference(f'{guild.id}/Meets')
                ref.child(f'{day.lower()} {start}').update({
                    f'{code}': f'{end}',
                })

                await ctx.send(f'>>> Class meet was added on "{day}" at time "{start}" to "{end}"')
        else:
            #Adds meet to blocks
            ref.child(f'{day.lower()} {start}').set({
                'Start': f'{start}',
                'End': f'{end}'
            })

            #Adds class to meets
            ref = client.db.reference(f'{guild.id}/Meets')
            ref.child(f'{day.lower()} {start}').update({
                f'{code}': f'{end}',
            })

            await ctx.send(f'>>> Class meet was added on "{day}" at time "{start}" to "{end}"')
    else:
        await ctx.send(f'>>> No class was found with code: "{code}"')
        