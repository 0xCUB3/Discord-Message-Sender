import discord
from discord.ext import tasks

client = discord.Client()

# CHANGE ME
token = "YOUR DISCORD BOT TOKEN HERE"
message = "YOUR MESSAGE HERE"
channel_id = 000000000000 # Replace with your channel ID

@tasks.loop(minutes=10)
async def test():
    channel = client.get_channel(929866206234677279)
    await channel.send(message)

@client.event
async def on_ready():
    test.start()

client.run(token)