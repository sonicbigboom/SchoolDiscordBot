#Client
import client

#Events


#Commands
import ping_command

#Config
import config

@client.client.event
async def on_ready(): 
    print('Bot is ready.')

client.client.run(config.TOKEN)

#pls dont roast me for this
#actually so overcomplicated, you only need like 4 commands for the bot lol

