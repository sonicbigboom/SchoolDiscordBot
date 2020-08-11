import discord
from discord.ext import commands

import checks

client = commands.Bot(command_prefix = '$')
print("Setting up discord client...")

client.owner_ids = {
    264099995916042240,
    277883722852728832,
    307264624506568704
}

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {

    'databaseURL': 'https://school-discord-bot.firebaseio.com/'

})

#Adding to the database
'''
ref = db.reference('/')
ref.set({

    'Employee': 
        {
            'emp1': {
                'name':'Ido',
                'lname':'Shoshani',
                'age':17
            },

            'emp2': {
                'name':'Alex',
                'lname':'Zhang',
                'age':16
            }

        }
        

})
'''

#Updating the database
'''
ref = db.reference('Employee')

ref.update({

    'emp1/lname':'last1',
    'emp2/lname':'last2'

})
'''


#Get database data

ref = db.reference('Employee')
print(ref.get())