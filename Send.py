import discord
from dotenv import load_dotenv
from config import ds_config,sr_config
import asyncio


load_dotenv()
client = discord.Client()
token = ds_config["DISCORD_TOKEN"]


@client.event
async def try_out():
    await asyncio.sleep(sr_config["Sleep btw searches"])
    while (True):
        Channel = client.get_channel(ds_config["DISCORD_CHANEL"])
        f = open('toOut.txt', 'r')
        lines = f.readlines()
        for line in lines:
            if line!="":
                await Channel.send(line)
        f.close()
        f = open('toOut.txt', 'w')
        f.write("")
        f.close()
client.loop.create_task(try_out())
client.run(token)