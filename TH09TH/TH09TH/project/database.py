import mysql.connector

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="demo"
            )
            self.cursor = self.conn.cursor()
            print("✅ Kết nối MySQL thành công!")  # In thông báo nếu kết nối thành công
        except mysql.connector.Error as err:
            print(f"❌ Lỗi kết nối MySQL: {err}")  # Báo lỗi nếu kết nối thất bại
            self.conn = None
            self.cursor = None

    def execute(self, query, params=None):
        if self.conn is None:
            print("⚠️ Không thể thực hiện truy vấn vì chưa kết nối CSDL.")
            return
        try:
            self.cursor.execute(query, params or ())
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"❌ Lỗi SQL: {err}")

    def fetch_one(self, query, params=None):
        if self.conn is None:
            print("⚠️ Không thể lấy dữ liệu vì chưa kết nối CSDL.")
            return None
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"❌ Lỗi khi lấy dữ liệu: {err}")
            return None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("🔌 Đã đóng kết nối MySQL.")
