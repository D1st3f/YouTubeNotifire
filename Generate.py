from time import sleep
from config import yt_config, sr_config
import requests
from sql_cheack import add_and_cheack_video

chanel = 1

def get_last_videos():
    a = ""
    name = ""
    for line in requests.get(yt_config["Youtube Link"][chanel-1]).text.split(
            "\n"):
        if "/*# sourceMappingURL=kevlar_global_styles_sass.css.map" in line:
            a = line
        if '<link itemprop="name" content=' in line:
            name = (line[line.find('<link itemprop="name" content=') + 31:line.find('"></span><script')])
    b = a.split('{')
    last_videos = []
    for i in range(0, len(b) - 8):
        if '"accessibility":' in b[i]:
            if '"accessibilityData":' in b[i + 1] and '"publishedTimeText"' in b[i + 2]:
                last_videos.append([name, b[i + 2][9:b[i + 2].find(" автор:")], "https://www.youtube.com" + b[i + 7][b[
                                                                                                                         i + 7].find(
                    '"url":"') + 7:b[i + 7].find('","webPageType"')]])
    last_videos.reverse()
    return last_videos


def write_to_user(new_videos):
    if new_videos != []:
        f = open('toOut.txt', 'a', encoding="utf-8")
        for new_video in new_videos:
            f.write(
                f"У {new_video[0]} з'явилося нове відео: {new_video[1]}. Покликання на відео: {new_video[2]}" + "\n")
        f.close()
    else:
        print("pass")


while True:
    last_videos = get_last_videos()
    new_videos = add_and_cheack_video(last_videos, chanel)
    write_to_user(new_videos)
    sleep(sr_config["Sleep btw searches"])
    if chanel == len(yt_config["Youtube Link"]):
        chanel = 1
    else:
        chanel+=1
