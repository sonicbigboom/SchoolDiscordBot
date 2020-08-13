import client

@client.client.command()
@client.checks.is_admin()
async def meets(ctx, arg):
    message = ctx.message
    author = ctx.author
    guild = ctx.guild

    ref = client.db.reference(f'{guild.id}/Meets')

    result = "Meets:\n"

    for key, value in ref.get().items():
        dayAndStart = key
        meetData = value

        if arg in meetData:
            result += "     "
            result += dayAndStart
            result += " - "
            result += meetData[f'{arg}']
            result += "\n"
        
    await ctx.send(f'>>> {result}')

    
    