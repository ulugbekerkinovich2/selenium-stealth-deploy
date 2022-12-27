# import speedtest module
import requests
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
    print(all_data)
    return all_data


# cursor = connection.cursor()
# cursor.execute("SELECT * FROM upload_data")
# all_data = cursor.fetchall()
# print(all_data)
def telebots(mess):
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess}")


def telebots2(mess, mess1):
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess}")
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess1}")


def telebots3(mess, mess1, mess2):
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess}")
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess1}")
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess2}")


def telebots4(mess, mess1, mess2, mess3, mess4):
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess}")
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess1}")
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess2}")
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess3}")
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAF8nrZbyM1DQ1RHYse5t0X3F40vTpYsssA/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess4}")
