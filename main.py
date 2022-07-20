from datetime import time
from config import yt_config , ds_config
from requests_html import HTMLSession


def get_html():
    try:
        session = HTMLSession()
        r = session.get(yt_config["Youtube Link"])
        r.html.render()
        return r
    except:
        print("BAD TRY TO REACH SITE !" + "\n" +"NEXT TRY AFTER 5 SECOUNDS !")
        time.sleep(5)
    return ""

def get_last_videos(html):
    r = html
    videos = r.html.xpath('//*[@id="video-title"]')
    name_of_channel = r.html.xpath('//*[@id="text-container"]', first=True).text
    last_videos =  []
    for video in videos:
        last_videos.append([name_of_channel, video.text, ("https://www.youtube.com/"+str(video.links)[2:-2])])
    return last_videos

html = get_html()
while html == "":
    html = get_html()
last_videos = get_last_videos(html)
print(last_videos[0][1])
# add_and_cheack_video(last_videos)


