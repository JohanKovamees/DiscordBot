import discord
import logging
import os
import requests
import json

logging.basicConfig(level=logging.INFO)
TOKEN = (os.environ['TOKEN'])
print('The app token is:')
print(TOKEN)
client = discord.Client()

def get_quote():
    response = requests.get("https://stoicquotesapi.com/v1/api/quotes/random")
    jsonData = json.loads(response.text)
    quote = jsonData['body'] + " -" + jsonData['author']
    return(quote)

def get_cur(cur1, cur2):
    response = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur.json")
    val1 = response[cur1]
    val2 = response[cur2]
    converted_value = val2//val1
    return("1 " + cur1 " = " + converted_value + " " + cur2)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send('''This bot has the following options:
        !wisdom --- Generates a stoic qoute \n
        \n
        Or you can just try saying "Hello"
        ''')

    if message.content.startswith('!wisdom'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('!currency')

    if message.content.startswith('Hello'):
        await message.channel.send('Hello human trash!')

    if message.content.startswith('Trash'):
        await message.channel.send('NO U')

client.run(TOKEN)
