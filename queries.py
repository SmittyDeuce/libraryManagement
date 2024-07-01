import mysql.connector
from mysql.connector import Error

def connect_database():

    db_name = "library_db"
    user = "root"
    password = "Ibewlu332$@$!!"
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