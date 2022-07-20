from config import db_config
import mysql.connector
from mysql.connector import errorcode


def print_all():
    try:
        cnx = mysql.connector.connect(user=db_config["test_sql123"]["user"],
                                      password=db_config["test_sql123"]["password"],
                                      host=db_config["test_sql123"]["host"],
                                      database="test_sql123")
        cursor = cnx.cursor()
        cursor.execute(f"SELECT * FROM youtube_videos")
        serched = cursor.fetchall()
        for video in serched:
            print(video)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
