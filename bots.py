from print_all_info import print_all


def send_to_user(new_videos):
    if new_videos != []:
        for new_video in new_videos:
            print(f"У {new_video[0]} з'явилося нове відео: {new_video[1]}. Покликання на відео: {new_video[2]}")
    else:
        print_all()
