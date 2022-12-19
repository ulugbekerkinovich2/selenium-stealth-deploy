import psycopg2
from django.conf.global_settings import DATABASES

connect = psycopg2.connect(DATABASES)
connect.autocommit = True
cursor = connect.cursor()