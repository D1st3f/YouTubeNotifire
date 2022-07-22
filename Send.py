import discord
import telegram
from dotenv import load_dotenv
from config import ds_config, sr_config, tg_config
import asyncio

bot = telegram.Bot(tg_config["TELEGRAM_TOKEN"])
load_dotenv()
client = discord.Client()
token = ds_config["DISCORD_TOKEN"]
TOKEN = tg_config["TELEGRAM_TOKEN"]


@client.event
async def try_out():
    await asyncio.sleep(sr_config["Sleep btw searches"])
    while (True):
        Channel = client.get_channel(ds_config["DISCORD_CHANEL"])
        f = open('toOut.txt', 'r')
        lines = f.readlines()
        for line in lines:
            if line != "":
                bot.sendMessage(chat_id=tg_config["TELEGRAM_CHANEL"], text=line)
                await Channel.send(line)
        f.close()
        f = open('toOut.txt', 'w')
        f.write("")
        f.close()


client.loop.create_task(try_out())
client.run(token)
