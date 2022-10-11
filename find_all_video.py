from config import yt_config, send_config
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
            if ('"accessibilityData":' in b[i + 1] and '"runs":[' in b[i + 3]) or (
                    '"accessibilityData":' in b[i + 1] and 'clickTrackingParams' in b[i + 3]):
                limk = ""
                for c in range(0, 15):
                    if '"url":"' in b[i + c]:
                        limk = ("https://www.youtube.com" + b[i + c][b[i + c].find('"url":"') + 7:b[i + c].find(
                            '","webPageType"')])
                        break
                last_videos.append([name, b[i + 2][9:b[i + 2].find(" автор:")], limk])
    return last_videos


def get_all_video(chanel):
    last_videos = get_last_videos(chanel)
    if send_config["Reverse"]==True:
        last_videos.reverse()
    return last_videos
