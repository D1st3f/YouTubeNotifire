from time import sleep
from config import yt_config, ds_config, sr_config
from requests_html import HTMLSession
from sql_cheack import add_and_cheack_video
from bots import send_to_user


def get_html():
    session = HTMLSession()
    r = session.get(yt_config["Youtube Link"])
    r.html.render()
    return r


def get_last_videos(html):
    try:
        r = html
        videos = r.html.xpath('//*[@id="video-title"]')
        name_of_channel = r.html.xpath('//*[@id="text-container"]', first=True).text
        last_videos = []
        for video in videos:
            last_videos.append([name_of_channel, video.text, ("https://www.youtube.com/" + str(video.links)[2:-2])])
        last_videos.reverse()
        return last_videos
    except:
        return "SOMETHING WRONG !"


while True:
    html = get_html()
    last_videos = get_last_videos(html)
    if last_videos != "SOMETHING WRONG !":
        last_videos = get_last_videos(html)
        new_videos = add_and_cheack_video(last_videos)
        send_to_user(new_videos)
        sleep(sr_config["Sleep btw searches"])
    else:
        pass
