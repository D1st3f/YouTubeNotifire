#   pip install mysql-connector-python
#   pip install discord.py
#   pip install python-telegram-bot
#   pip install python-dotenv

yt_config = {
    "Youtube Link": ["https://www.youtube.com/channel/UCTZKGpLLemdjKZxV6owQPrg/videos",  # soloWay gaming
                     "https://www.youtube.com/c/TonyPersitski/videos",  # Tony Persitski
                     "https://www.youtube.com/c/OLDboiUA/videos",  # OLDboi
                     "https://www.youtube.com/c/STERNENKO/videos",  # STERNENKO
                     "https://www.youtube.com/c/uttoronto/videos",  # Телебачення Торонто
                     "https://www.youtube.com/c/GeekJournal/videos",  # Geek Journal
                     "https://youtube.com/c/PlayStationGrenade/videos",  # PlayStationGrenade
                     "https://youtube.com/c/PlayStation/videos",  # PlayStation
                     "https://youtube.com/c/xbox/videos",  # Xbox
                     "https://youtube.com/channel/UCi0Z9L9HrhD7oYpMs2pLxSw/videos",  # Всесвіт UA
                     "https://youtube.com/c/AdrianZPcity/videos",  # AdrianZP
                     "https://www.youtube.com/c/IGN/videos",  # IGN
                     "https://www.youtube.com/c/AMD/videos",  # AMD
                     "https://www.youtube.com/c/gamespot/videos",  # GameSpot
                     "https://www.youtube.com/user/PlayUAmain/videos",  # PlayUA
                     "https://www.youtube.com/channel/UCr7r1-z79TYfqS2IPeRR47A/videos",  # ROZETKA
                     "https://www.youtube.com/c/%D0%97%D0%B0%D0%B3%D1%96%D0%BD%D0%9A%D1%96%D0%BD%D0%BE%D0%BC%D0%B0%D0%BD%D1%96%D0%B2/videos",
                     # Загін Кіноманів
                     "https://www.youtube.com/channel/UCC1NDWUoOELGpgAaaA5wCxg/videos",  # Огляд UA
                     "https://www.youtube.com/c/AZOVmedia/videos",  # AZOV media
                     "https://www.youtube.com/c/GameStreetUA/videos",  # GameStreetUA
                     "https://www.youtube.com/c/KolegiStudio/videos",  # Kolegi Studio!
                     "https://www.youtube.com/channel/UClfvPggDeOOYvmYggsAbvLg/videos",  # PlayStation Україна
                     "https://www.youtube.com/c/cikavanauka/videos",  # Цікава наука
                     "https://www.youtube.com/c/NVIDIA/videos",  # NVIDIA
                     "https://www.youtube.com/c/MrBeast6000/videos",  # MrBeast
                     "https://www.youtube.com/c/%D0%9A%D0%B0%D0%BD%D0%B0%D0%BB%D0%93%D0%BE%D1%80%D0%BE%D0%B1%D0%B8%D0%BD%D0%B0/videos",
                     # Канал Горобина
                     "https://www.youtube.com/c/%D0%9B%D0%AC%D0%92%D0%AB%D0%9D%D0%90%D0%94%D0%96%D0%98%D0%9F%D0%95/videos",
                     # ЛЬВЫ НА ДЖИПЕ
                     "https://www.youtube.com/c/MarkusUA/videos",  # MARKUS
                     "https://www.youtube.com/c/TA_studioo/videos",  # TA
                     ]}

ds_config = {
    "DISCORD_TOKEN": "INSERT YOUR TOKEN HERE",
    "DISCORD_CHANEL": [["INSERT YOUR CHANEL HERE", "SendEveryChannelVideo"]  # DISCORD CHANEL ID AND FILTER
                      ]
}

tg_config = {
    "TELEGRAM_TOKEN": "INSERT YOUR TOKEN HERE",
    "TELEGRAM_CHANEL": [["INSERT YOUR CHANEL HERE", "OLDboi", "Tony Persitski", "soloWay gaming", "STERNENKO", "Телебачення Торонто", "Geek Journal", "ROZETKA", "AZOV media", "Kolegi Studio!", "PlayStation Україна", "MrBeast", "Канал Горобина", "MARKUS", "ТА"]
                        ]   # TELEGRAM CHANEL ID AND FILTER
}

sr_config = {
    "Sleep btw searches": 2  # set delay between searches
}

send_config = {
    "Debug_mode": False  # set True and you will not send messages
}

db_config = {
    "my_db": {
        "database": "my_db",
        "host": "hp.local",
        "user": "root",
        "password": "root",
        "table": "YouTube_"
    }
}
