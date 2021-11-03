import discord
import logging
import os

logging.basicConfig(level=logging.INFO)
TOKEN = (os.environ['TOKEN'])
print('The app token is:')
print(TOKEN)
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello bot'):
        await message.channel.send('Hello human trash!')

    if message.content.startswith('Hello'):
        await message.channel.send('Hello human trash!')

    if message.content.startswith('Trash'):
        await message.channel.send('NO U')

client.run(TOKEN)
