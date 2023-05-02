import instaloader
import pandas as pd
import discord
from discord.ext import tasks
import datetime as dt
from discord import Intents
import pickle

discord_token = "YOUR DISCORD TOKEN"  

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

igbot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(igbot.context, 'IG USERNAME')

amount_filename = "amount.pickle"
is_sent = False

def save_amount(amount):
    with open(amount_filename, 'wb') as f:
        pickle.dump(amount, f)

def load_amount():
    try:
        with open(amount_filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return 569

async def check_followers():
    global is_sent
    amount = load_amount()
    if not is_sent and profile.followers > amount:
        is_sent = True
        amount += 1 # Set here deafult amount
        save_amount(amount)
        embed = discord.Embed(title=amount)
        sent = await client.get_channel(CHANNEL ID).send(embed=embed)


@client.event
async def on_ready():
    await check_followers()
    

if __name__ == "__main__":
    client.run(discord_token)