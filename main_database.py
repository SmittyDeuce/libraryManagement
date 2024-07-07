import mysql.connector
from mysql.connector import Error

def connect_database():

    db_name = "library_db"
    user = "root"
    password = ""
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        print("Connection to database successful")
        return conn
    
    except Error as e:
        print(f"Error: {e}")
        return None
    
# connect_database()


def close_database(conn):
    if conn:
        conn.close()
        print("Connection to database closed")