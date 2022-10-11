import datetime
import pytz
import telegram
from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
import requests
from config import ds_config, tg_config, send_config

bot = telegram.Bot(tg_config["TELEGRAM_TOKEN"])


def deescape(escaped):
    return escaped.replace("\\u0026", "&")


def prepare_telegram(name, text, link):
    return "<b>У " + deescape(name) + " з'явилося нове " + 'відео. &#13;&#10;</b><a href="'+ deescape(link) + '">' + \
           deescape(text) + "</a>"


def send_telegram(video):
    if send_config["Debug_telegram"] == False:
        for i in tg_config["TELEGRAM_CHANEL"]:
            text_tg = prepare_telegram(video[0], video[1], video[2])

            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="📺 ПЕРЕГЛЯНУТИ", url=video[2]),
                 InlineKeyboardButton(text="🇺🇦 ПІДТРИМАТИ",
                                      url="https://savelife.in.ua/donate/#donate-army-card-once")],
            ])

            if "SendEveryChannelVideo" in i:
                bot.sendPhoto(chat_id=i[0], photo=find_tumb(video[2]), caption=text_tg, parse_mode=ParseMode.HTML,
                              reply_markup=keyboard)

            elif deescape(video[0]) in i:
                bot.sendPhoto(chat_id=i[0], photo=find_tumb(video[2]), caption=text_tg, parse_mode=ParseMode.HTML,
                              reply_markup=keyboard)

def find_tumb(url):
    url = url.replace('https://www.youtube.com/watch?v=', '')
    url = url.replace("https://www.youtube.com/shorts/", "")
    t = requests.get(f"https://img.youtube.com/vi/{url}/maxresdefault.jpg")
    if not t:
        t = requests.get(f"https://img.youtube.com/vi/{url}/hqdefault.jpg")
        if not t:
            t = requests.get(f"https://img.youtube.com/vi/{url}/mqdefault.jpg")
            if not t:
                t = requests.get(f"https://img.youtube.com/vi/{url}/sddefault.jpg")
                if not t:
                    return f"https://img.youtube.com/vi/{url}/sddefault.jpg"
                else:
                    return f"https://img.youtube.com/vi/{url}/sddefault.jpg"
            else:
                return f"https://img.youtube.com/vi/{url}/mqdefault.jpg"
        else:
            return f"https://img.youtube.com/vi/{url}/hqdefault.jpg"
    else:
        return f"https://img.youtube.com/vi/{url}/maxresdefault.jpg"


def prepare_discord(name, text, link):
    thunb_link = find_tumb(link)
    messege = {
        "username": "NotiBot",
        "avatar_url": "https://ih1.redbubble.net/image.3081029279.3778/raf,750x1000,075,t,fafafa:ca443f4786.u1.jpg"
    }
    messege["embeds"] = [
        {
            "title": f"**У {deescape(name)} з'явилося нове відео.**",
            "description": f"**[{deescape(text)}]({link})**",
            "color": 16711680,
            "footer": {
                "text": "D1st3f",
                "icon_url": "https://avatars.cloudflare.steamstatic.com/a6c9583e31c83ab1359da45864c054077d8b09c7_full.jpg"
            },
            "timestamp": datetime.datetime.now().astimezone(pytz.UTC).strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            "image": {
                "url": thunb_link
            }
        }
    ]
    messege["components"] = [
    {
      "type": 1,
      "components": [
        {
          "type": 2,
          "style": 5,
          "emoji": {"id": "873300749700972594","name": "YouTube"},
          "label": " ПЕРЕГЛЯНУТИ",
          "url": link
        },
        {
          "type": 2,
          "style": 5,
          "emoji": {"id": "873300749898104893", "name": "UKR"},
          "label": " ПІДТРИМАТИ",
          "url": "https://savelife.in.ua/donate/#donate-army-card-once"
        }
      ]
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

