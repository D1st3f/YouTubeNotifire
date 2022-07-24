from config import db_config
import mysql.connector
from mysql.connector import errorcode


def def_table(cursor, cnx, channel):
    table_name = db_config["my_db"]["table"] + str(channel)
    cursor.execute(f'''
           CREATE TABLE IF NOT EXISTS {table_name} (
          `id` int(11)  NOT NULL AUTO_INCREMENT,
          `name` TEXT NOT NULL,
          `text` TEXT NOT NULL,
          `link` TEXT NOT NULL,
          PRIMARY KEY (`id`)) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4''')
    cnx.commit()


def add_new_video(video, cursor, cnx, channel):
    table_name = db_config["my_db"]["table"] + str(channel)
    cursor.execute(f"SELECT COUNT(link) FROM {table_name} WHERE link='{video[2]}'")
    serched = cursor.fetchall()
    if int(str(serched[0])[1:-2]) == 0:
        cursor.execute(f"INSERT INTO {table_name} (name,text,link) VALUES ('{video[0]}','{video[1]}','{video[2]}')")
        cnx.commit()
        return video
    else:
        return None


def add_and_cheack_video(last_videos, channel):
    try:
        cnx = mysql.connector.connect(user=db_config["my_db"]["user"],
                                      password=db_config["my_db"]["password"],
                                      host=db_config["my_db"]["host"],
                                      database="my_db",
                                      )
        cursor = cnx.cursor()
        def_table(cursor, cnx, channel)
        new_video = []
        for video in last_videos:
            while "'" in video[0]:
                video[0] = video[0].replace("'", "")
            while "'" in video[1]:
                video[1] = video[1].replace("'", "")
            while '"' in video[0]:
                video[0] = video[0].replace('"', "")
            while '"' in video[1]:
                video[1] = video[1].replace('"', "")
            if add_new_video(video, cursor, cnx, channel) != None:
                new_video.append(video)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
        return new_video
