# YouTubeNotifire 🇺🇦
![This is an image](https://img08.rl0.ru/afisha/e1200x600i/daily.afisha.ru/uploads/images/8/e3/8e3a431d6aed005bdb4dccabc1f719b1.jpg)

## About 
 This script can send notification from any [YouTube](https://www.youtube.com/) channel. You can add any number of channel where script must take information.
 Sript can send notification to Telegram and Discord channels. Every chanel have custom setting, you can select from what chanels you want take noty.
 
## License

YouTubeNotifire is licensed under the MIT license. Refer to [LICENSE](LICENSE)  for more information.


## Running

Copy the latest git release and unpack it in the desired location. To run you nead install:
  *  [Python 3](https://www.python.org/downloads/)
  *  MySQL Connector - "_**pip install mysql-connector-python**_"
  *  Discord Bot - "_**pip install discord.py**_"
  *  Telegram Bot - "_**pip install python-telegram-bot**_"
  *  Python Dotenv - "_**pip install python-dotenv**_"

## How to config
* You nead to extract files to any your folder
 * Than go to "**_config.py_**"
 * Insert YouTube links, Discrod Bot Token, Telegram Bot Token, Discord Chenals id, Telegram Chanels id and cinfigurate filter what notification neeed to send, if you need all messages add "**_SendEveryChannelVideo_**" or if you want some custom chanels print names like - "**_"OLDboi", "Tony Persitski", "soloWay gaming"_**"
 * Don't forget to connect MySQL Databse in "**_config.py_**"
 * To create and fill database in "**_config.py_**" set "**_"Debug_mode" = True_**" and run  "**_main.py_**". Than cheack your DB.
 * After that you can set "**_"Debug_mode" = False_**"
 * In "**_config.py_**" - "**_"Sleep btw searches"_ = 2**" you can set delay between serches.
 
## How to use
 * Do "**_CONFIG_**"
 * At the end just run "**_main.py_**".

 ## Result 
 * You will take infinity loop of checking and sending notification to a lot channels from alot YouTube links, what you can configurate.

# Happy Watching 😍
 


