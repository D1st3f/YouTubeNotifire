import discord
import telegram
from dotenv import load_dotenv
from config import ds_config, sr_config, tg_config, yt_config
from find_new_video import add_and_cheack_video
import asyncio
from find_all_video import ggeet

bot = telegram.Bot(tg_config["TELEGRAM_TOKEN"])
load_dotenv()
client = discord.Client()
token = ds_config["DISCORD_TOKEN"]
TOKEN = tg_config["TELEGRAM_TOKEN"]


@client.event
async def try_out():
    chanel = 1
    while (True):
        Channel = client.get_channel(ds_config["DISCORD_CHANEL"])
        await asyncio.sleep(sr_config["Sleep btw searches"])
        last_video = ggeet(chanel)
        new_video = add_and_cheack_video(last_video, chanel)
        if chanel == len(yt_config["Youtube Link"]):
            chanel = 1
        else:
            chanel += 1
        for video in new_video:
            text = f"У {video[0]} з'явилося нове відео: {video[1]}. Покликання на відео: {video[2]}" + "\n"
            bot.sendMessage(chat_id=tg_config["TELEGRAM_CHANEL"], text=text)
            await Channel.send(f"У {video[0]} з'явилося нове відео: {video[1]}. Покликання на відео: {video[2]}" + "\n")


client.loop.create_task(try_out())
client.run(token)
