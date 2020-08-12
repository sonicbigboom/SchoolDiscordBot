#Client
import client

#Events


#Commands
import ping_command
import init_command
import create_command
import join_command
import stop_command
import add_command
import classes_command
import meets_command

#Config
import config

@client.client.event
async def on_ready(): 
    print('Bot is ready.')
    print(client.client.owner_ids)

client.client.run(config.TOKEN)

#pls dont roast me for this
#actually so overcomplicated, you only need like 4 commands for the bot lol

