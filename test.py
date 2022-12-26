# import speedtest module
import speedtest
from django.db import connection


# def speedtest1():
#     speed_test = speedtest.Speedtest()
#     upload_speed = speed_test.upload()
#     print("Your Upload speed is", upload_speed / 1024 ** 2)
#     speed = upload_speed / 1024 ** 2
#     return speed

def wait_t():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM upload_data")
    all_data = cursor.fetchall()
    # print(all_data)
    return all_data


# cursor = connection.cursor()
# cursor.execute("SELECT * FROM upload_data")
# all_data = cursor.fetchall()
# print(all_data)
