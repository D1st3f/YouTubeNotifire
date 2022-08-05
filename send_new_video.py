import datetime
import pytz
import telegram
from telegram import ParseMode
import requests
from config import ds_config, tg_config, send_config

bot = telegram.Bot(tg_config["TELEGRAM_TOKEN"])


def deescape(escaped):
    return escaped.replace("\\u0026", "&")


def prepare_telegram(name, text, link):
    return "<b>У " + deescape(name) + " з'явилося нове " + 'відео - </b><a href="' + deescape(link) + '">' + \
           deescape(text) + ".</a>"


def send_telegram(video):
    if send_config["Debug_telegram"] == False:
        for i in tg_config["TELEGRAM_CHANEL"]:
            text_tg = prepare_telegram(video[0], video[1], video[2])
            if "SendEveryChannelVideo" in i:
                bot.sendMessage(chat_id=i[0], text=text_tg, parse_mode=ParseMode.HTML)
            elif deescape(video[0]) in i:
                bot.sendMessage(chat_id=i[0], text=text_tg, parse_mode=ParseMode.HTML)


def prepare_discord(name, text, link):
    messege = {
        "username": "NotiBot",
        "avatar_url": "https://ih1.redbubble.net/image.3081029279.3778/raf,750x1000,075,t,fafafa:ca443f4786.u1.jpg"
    }
    messege["embeds"] = [
        {
            "title": f"**У {deescape(name)} з'явилося нове відео.**",
            "description": f"**[{deescape(text)}]({link})**",
            "url": link,
            "color": 16711680,
            "footer": {
                "text": "D1st3f",
                "icon_url": "https://avatars.cloudflare.steamstatic.com/a6c9583e31c83ab1359da45864c054077d8b09c7_full.jpg"
            },
            "timestamp": datetime.datetime.now().astimezone(pytz.UTC).strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            "image": {
                "url": f"https://i3.ytimg.com/vi/{link.replace('https://www.youtube.com/watch?v=', '')}/maxresdefault.jpg"
            }
        }
    ]
    return messege


def send_discord(video):
    if send_config["Debug_discord"] == False:
        for i in ds_config["DISCORD_CHANEL"]:
            if "SendEveryChannelVideo" in i:
                messege = prepare_discord(video[0], video[1], video[2])
                result = requests.post(url=i[0], json=messege)
                try:
                    result.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(err)
            elif deescape(video[0]) in i:
                messege = prepare_discord(video[0], video[1], video[2])
                result = requests.post(url=i[0], json=messege)
                try:
                    result.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(err)


def send_new_video(new_video):
    if send_config["Debug_mode"] == False:
        if new_video:
            for video in new_video:
                send_telegram(video)
                send_discord(video)
                if send_config["Telefram_debud"]:
                    bot.sendMessage(chat_id=send_config["Telegram_debug_channel"], text=f"Finded {video[1]}")
        else:
            if send_config["Telefram_debud"]:
                bot.sendMessage(chat_id=send_config["Telegram_debug_channel"], text="Cheacked")

