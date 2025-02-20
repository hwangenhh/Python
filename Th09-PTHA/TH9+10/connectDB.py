import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"
        )
        if conn.is_connected():
            print("Kết nối MySQL thành công!")
            return conn
    except Error as e:
        print(f"Lỗi kết nối MySQL: {e}")
        return None
