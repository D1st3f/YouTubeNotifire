from config import yt_config
from find_new_video import get_new_video
from find_all_video import get_all_video
from send_new_video import send_new_video

for chanel in range(1, len(yt_config["Youtube Link"])):
    last_video = get_all_video(chanel)
    new_video = get_new_video(last_video, chanel)
    send_new_video(new_video)
