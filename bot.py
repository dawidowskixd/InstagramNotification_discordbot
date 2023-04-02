import instaloader
import pandas as pd
import discord
from discord.ext import tasks
import datetime as dt
from discord import Intents

discord_token = "YOUR DISCORD BOT TOKEN"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

igbot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(igbot.context, 'YOUR INSTAGRAM USERNAME')

is_sent = False

@tasks.loop(minutes=1)
async def check_followers():
    global is_sent
    if not is_sent and profile.followers != 567:
        embed = discord.Embed(title="MESSAGE YOU WANT TO GET")
        sent = await client.get_channel(*CHANNEL ID*).send(embed=embed)
        is_sent = True

@client.event
async def on_ready():
    check_followers.start()

if __name__ == "__main__":
    client.run(discord_token)




#MTA5MjEzNDI2OTM4MTUxNzMxMw.GMcg8d.GCax5V7gnSjEo3SdQyXXXJz7X5_NKRnZcp9WX0