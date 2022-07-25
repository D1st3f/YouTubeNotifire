import telegram
import asyncio
import discord
from dotenv import load_dotenv
from telegram import ParseMode
from config import ds_config, sr_config, tg_config, yt_config, send_config
from find_new_video import get_new_video
from find_all_video import get_all_video

bot = telegram.Bot(tg_config["TELEGRAM_TOKEN"])
load_dotenv()
client = discord.Client()
token = ds_config["DISCORD_TOKEN"]
TOKEN = tg_config["TELEGRAM_TOKEN"]


def deescape(escaped):
    return escaped.replace("\\u0026", "&")


def prepare_telegram(name, text, link):
    return "<b>У " + name + " з'явилося нове" + 'відео - </b><a href="' + link + '">' + text + ".</a>"


def prepare_discord(name, text, link):
    return f"У {name} з'явилося нове відео: {text}. Покликання на відео: {link}" + "\n"


@client.event
async def try_out():
    chanel = 1
    while (True):

        await asyncio.sleep(sr_config["Sleep btw searches"])
        last_video = get_all_video(chanel)
        new_video = get_new_video(last_video, chanel)
        if chanel == len(yt_config["Youtube Link"]):
            chanel = 1
        else:
            chanel += 1
        if send_config["Debug_mode"] == False:
            for video in new_video:
                name = deescape(video[0])
                text = deescape(video[1])
                link = video[2]
                for i in tg_config["TELEGRAM_CHANEL"]:
                    text_tg = prepare_telegram(name, text, link)
                    if "SendEveryChannelVideo" in i:
                        bot.sendMessage(chat_id=i[0], text=text_tg, parse_mode=ParseMode.HTML)
                    elif name in i:
                        bot.sendMessage(chat_id=i[0], text=text_tg, parse_mode=ParseMode.HTML)
                for i in ds_config["DISCORD_CHANEL"]:
                    text_ds = prepare_discord(name, text, link)
                    Channel = client.get_channel(i[0])
                    if "SendEveryChannelVideo" in i:
                        await Channel.send(text_ds)
                    elif name in i:
                        await Channel.send(text_ds)


client.loop.create_task(try_out())
client.run(token)
