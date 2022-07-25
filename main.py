import telegram
import asyncio
import discord
from dotenv import load_dotenv
from config import ds_config, sr_config, tg_config, yt_config, send_config
from find_new_video import add_and_cheack_video
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

        await asyncio.sleep(sr_config["Sleep btw searches"])
        last_video = ggeet(chanel)
        new_video = add_and_cheack_video(last_video, chanel)
        if chanel == len(yt_config["Youtube Link"]):
            chanel = 1
        else:
            chanel += 1
        if send_config["Debug_mode"] == False:
            for video in new_video:
                for i in tg_config["TELEGRAM_CHANEL"]:
                    bot.sendMessage(chat_id=i,
                                    text=f"У {video[0]} з'явилося нове відео: {video[1]}. Покликання на відео: {video[2]}" + "\n")
                for i in ds_config["DISCORD_CHANEL"]:
                    Channel = client.get_channel(i)
                    await Channel.send(
                        f"У {video[0]} з'явилося нове відео: {video[1]}. Покликання на відео: {video[2]}" + "\n")


client.loop.create_task(try_out())
client.run(token)
