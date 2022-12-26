import psycopg2
from django.conf.global_settings import DATABASES

connect = psycopg2.connect(
    host="127.0.0.1",
    database="postgres6",
    user="postgres",
    password="0852")
connect.autocommit = True
cursor = connect.cursor()


# cursor = connection.cursor()
# cursor.execute("SELECT * FROM upload_data")
# all_data = cursor.fetchone()
# print(all_data, type(all_data[8]))