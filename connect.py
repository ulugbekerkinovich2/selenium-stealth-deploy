import psycopg2
from django.conf.global_settings import DATABASES

connect = psycopg2.connect(
    host="127.0.0.1",
    database="postgres3",
    user="postgres",
    password="0852")
connect.autocommit = True
cursor = connect.cursor()