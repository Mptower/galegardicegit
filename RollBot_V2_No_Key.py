import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get 
import os
import random
import re

#below code gives bot permissions from discord API
intents = discord.Intents.default()
intents.messages = True 
intents.message_content = True
intents.members = True

#below code defines messages
messages = []

#below code activates the permissions recieved above
client = discord.Client(intents=intents)

#below code prints to terminal when on_ready is recieved from discord
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.listening, name='$Help'))

#below are the discord commands for rolling dice
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$Help'):
        await message.channel.send('Enter $ and whatever dice you want to roll in this manner $2D6. You can also add a modifier by using the + or - after is as such $2D6+3\n\nEnter $Drawcard to pull a card from the deck of many things')

    elif message.content.startswith('$Hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('$Critical'):
        await message.channel.send('The Adventure begins, they were always beside you, your nerdy best freinds and the DM to guide you!!')

    elif message.content.startswith('$Rick'):
        await message.channel.send("https://tenor.com/bEWOf.gif")

    elif message.content.startswith('$Drawcard'):
        list = ('the Sun card', 'the Void card', 'the Vizier card', 'the Moon card', 'the Star card', 'the Comet card', 'the Fates card', 'the Throne card', 'the Key card', 'the Knight card', 'the Gem card', 'the Talons card', 'the Flames card', 'the Skull card', 'the Idiot card', 'the Donjon card', 'the Ruin card', 'the Euryale card', 'the Rogue card', 'the Balance card', 'the Fool card', 'the Jester card' )
        await message.channel.send("You Drew " + random.choice(list))

    elif message.content.startswith('$'):
        try:
            total = 0
            output = "You Rolled "
            numOfDice = message.content[1]
            if '+' in message.content:
                dice = "(?<=D).*?(?=\+)"
                modifier = "\+(.*)"
                strValue = re.search(dice, message.content)
                strModifier = re.search(modifier, message.content)
                total += int(strModifier.group())
            elif '-' in message.content:
                dice = "(?<=D).*?(?=\-)"
                modifier = "\-(.*)"
                strValue = re.search(dice, message.content)
                strModifier = re.search(modifier, message.content)
                total += int(strModifier.group())
            else:
                dice = "(?<=D).*"
                strModifier = 0
                strValue = re.search(dice, message.content)
            for x in range(int(numOfDice)):
                roll = random.randint(1, int(strValue.group()))
                total += roll
                output += " " + str(roll)
            if '+' in message.content or '-' in message.content:
                await message.channel.send(str(output) + strModifier.group() + " = " + str(total))
            else:
                await message.channel.send(str(output) + " = " + str(total))
        except:
            print("an Input was made incorrectly")
            await message.channel.send("Input error, check input")

#token to connect client to discord - insert in string
client.run('')