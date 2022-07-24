from config import yt_config
import requests


def get_last_videos(chanel):
    last_videos = []
    a = ""
    name = ""
    for line in requests.get(yt_config["Youtube Link"][chanel - 1]).text.split("\n"):
        if "/*# sourceMappingURL=kevlar_global_styles_sass.css.map" in line:
            a = line
        if '<link itemprop="name" content=' in line:
            name = (line[line.find('<link itemprop="name" content=') + 31:line.find('"></span><script')])
    b = a.split('{')
    for i in range(0, len(b) - 8):

        if '"accessibility":' in b[i]:
            if '"accessibilityData":' in b[i + 1] and '"publishedTimeText"' in b[i + 2]:
                last_videos.append([name, b[i + 2][9:b[i + 2].find(" автор:")], "https://www.youtube.com" + b[i + 7][b[
                                                                                                                         i + 7].find(
                    '"url":"') + 7:b[i + 7].find('","webPageType"')]])
            if '"accessibilityData":' in b[i + 1] and '"runs":[' in b[i + 3]:
                limk = ("https://www.youtube.com" + b[i + 8][
                                                    b[i + 8].find('"url":"') + 7:b[i + 8].find('","webPageType"')])
                last_videos.append([name, b[i + 2][9:b[i + 2].find(" автор:")], limk])
    last_videos.reverse()
    return last_videos


def ggeet(chanel):
    last_videos = get_last_videos(chanel)
    return last_videos
