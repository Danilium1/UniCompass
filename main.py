import pandas
import psycopg2
from config import host, user, password, db_name

try:
    #тут мы подключаемся к бд
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name)
    # вместо постоянного коммит после каждого запроса
    #connection.autocommit = True
    with connection.cursor() as cursor:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT version();")
        print(f"Server version: {cursor.fetchone()}")
    with connection.cursor() as cursor:
        cursor = connection.cursor()
        cursor.execute(
            """CREATE TABLE users(
            id serial PRIMARY KEY,
            first_name varchar(50) NOT NULL,
            nick_name varchar(50) NOT NULL;"""
        )
        print(f"[INFO] Table created successfully")
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")


# df = pandas.read_excel(r"C:\Users\Danilium1\Downloads\TestForTable.xlsx")
# print(df)
#
# ages = df['years'].tolist()
# print(int(sum(ages)/len(ages)))

