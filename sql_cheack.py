from config import db_config
import mysql.connector
from mysql.connector import errorcode

table_name = db_config["YouTube"]["table"]


def def_table(cursor, cnx):
    cursor.execute(f'''
           CREATE TABLE IF NOT EXISTS {table_name} (
          `id` int(11)  NOT NULL AUTO_INCREMENT,
          `name` TEXT NOT NULL,
          `text` TEXT NOT NULL,
          `link` TEXT NOT NULL,
          PRIMARY KEY (`id`)) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4'''
                   )
    cnx.commit()


def add_new_video(video, cursor, cnx):
    cursor.execute(f"SELECT COUNT(link) FROM {table_name} WHERE link='{video[2]}'")
    serched = cursor.fetchall()
    if int(str(serched[0])[1:-2]) == 0:
        cursor.execute(f"INSERT INTO {table_name} (name,text,link) VALUES ('{video[0]}','{video[1]}','{video[2]}')")
        cnx.commit()
        return video
    else:
        return None


def add_and_cheack_video(last_videos):
    try:
        cnx = mysql.connector.connect(user=db_config["YouTube"]["user"],
                                      password=db_config["YouTube"]["password"],
                                      host=db_config["YouTube"]["host"],
                                      database="YouTube",
                                      port=8889)
        cursor = cnx.cursor()
        def_table(cursor, cnx)
        new_video = []
        for video in last_videos:
            if add_new_video(video, cursor, cnx) != None:
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
