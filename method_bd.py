import psycopg2
from config import host, user, password, db_name



#def create_table(str_with_data):
def create_table():
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name)
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor = connection.cursor()
            cursor.execute(
                """CREATE TABLE students(
                id serial PRIMARY KEY,
                name varchar(50) ,
                second_name varchar(100) ,
                age bigint,
                country varchar (100))"""
            )
            print(f"[INFO] Table created successfully")
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

def which_version_of_bd():
    try:
        #тут мы подключаемся к бд
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name)
        # вместо постоянного коммит после каждого запроса
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT version();")
            print( f"Server version: {cursor.fetchone()}")
    except Exception as _ex:
        print( "[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print( "[INFO] PostgreSQL connection closed")



def insert_into_table_gamno_variant(data_dict):
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name)
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor = connection.cursor()
            count_of_column = len(data_dict)
            columns_names = list(data_dict.keys())
            names_str = ', '.join(columns_names)
            full_row = []
            for i in range(count_of_column):
                name_of_column =  columns_names[i]
                for j in range(len(data_dict[name_of_column])):
                    full_row.append(data_dict.get(name_of_column)[j])
                    full_row = ', '.join(full_row)
                cursor.execute(
                    f"""INSERT INTO students ({names_str}) 
                    VALUES ({full_row}) """
                )
                full_row = []
            print(f"[INFO] Table created successfully")
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


def insert_into_table(data_list):
    try:
        #тут мы подключаемся к бд
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name)
        # вместо постоянного коммит после каждого запроса
        connection.autocommit = True

        cursor = connection.cursor( )
        for i in range(len(data_list)):
            data_row = data_list[i]
            cursor.execute("""INSERT INTO students (name, second_name, age, country)
            VALUES  (%s, %s, %s, %s)""", data_row)
        print(f"[INFO] Table created successfully")
    except Exception as _ex:
        print( "[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print( "[INFO] PostgreSQL connection closed")

def delete_students():
    try:
        #тут мы подключаемся к бд
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name)
        # вместо постоянного коммит после каждого запроса
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor = connection.cursor()
            cursor.execute(
                "TRUNCATE TABLE students;")
            print( f"Server version: {cursor.fetchone()}")
    except Exception as _ex:
        print( "[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print( "[INFO] PostgreSQL connection closed")



#"""INSERT INTO students (name, second_name, age, country)                     VALUES  (%s, %s, %s, %s)""", data_row