import client

@client.client.command()
@client.checks.is_admin()
async def classes(ctx):
    message = ctx.message
    author = ctx.author
    guild = ctx.guild

    ref = client.db.reference(f'{guild.id}/Classes')

    result = "Classes:\n"

    for key, value in ref.get().items():
        print(key)
        classCode = key
        className = value['Class Name']
        classTeacher = value['Teacher']

        if f'{author.id}' == f'{classTeacher}':
            result += "     "
            result += className
            result += "   "
            result += classCode
            result += "\n"
    
    print(result)
    await ctx.send(f'>>> {result}')
    
    