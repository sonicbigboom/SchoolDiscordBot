#Client
import client

#Events


#Commands
from Commands import ping_command
from Commands import init_command
from Commands import create_command
from Commands import join_command
from Commands import stop_command
from Commands import add_command
from Commands import classes_command
from Commands import meets_command

#Config
import config

@client.client.event
async def on_ready(): 
    print('Bot is ready.')
    print(client.client.owner_ids)

client.client.run(config.TOKEN)

