import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QTableWidgetItem, QInputDialog
from PyQt6.uic import loadUi
from datetime import datetime

class MenuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("D:\\Python\\Th09-PTHA\\TH09_TrangTTH\\main_ui.ui", self)
        self.btnStatistics = self.findChild(QPushButton, "btnStatistics")

        # Kết nối nút thống kê với hàm xử lý
        self.btnStatistics.clicked.connect(self.show_statistics)

        # Load dữ liệu ban đầu
        self.load_data()

    def connect_db(self):
        """Kết nối MySQL"""
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="test"
            )
            return db
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Lỗi kết nối", f"Không thể kết nối đến cơ sở dữ liệu: {err}")
            return None

    def load_data(self):
        """Load dữ liệu từ MySQL vào bảng tableMenu"""
        db = self.connect_db()
        if db is None:
            return

        cursor = db.cursor()
        cursor.execute("SELECT * FROM menu")
        rows = cursor.fetchall()
        db.close()

        self.tableMenu.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, value in enumerate(row_data):
                self.tableMenu.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def show_statistics(self):
        """Thống kê doanh thu theo tháng nhập"""
        try:
            # Hỏi người dùng nhập tháng và năm
            month, ok = QInputDialog.getInt(self, "Nhập tháng", "Nhập tháng cần thống kê (1-12):", min=1, max=12)
            year, ok2 = QInputDialog.getInt(self, "Nhập năm", "Nhập năm cần thống kê:", min=2000, max=datetime.now().year)

            if not ok or not ok2:
                return  # Thoát nếu người dùng không nhập

            db = self.connect_db()
            cursor = db.cursor()

            # Tổng số món ăn
            cursor.execute("SELECT COUNT(*) FROM menu")
            total_items = cursor.fetchone()[0]

            # Tổng doanh thu theo tháng nhập
            cursor.execute("""
                SELECT SUM(total_amount) 
                FROM orders 
                WHERE MONTH(order_date) = %s AND YEAR(order_date) = %s
            """, (month, year))
            monthly_revenue = cursor.fetchone()[0] or 0

            # Số đơn hàng trong tháng
            cursor.execute("""
                SELECT COUNT(*) 
                FROM orders 
                WHERE MONTH(order_date) = %s AND YEAR(order_date) = %s
            """, (month, year))
            total_orders = cursor.fetchone()[0]

            db.close()

            # Hiển thị kết quả thống kê
            stats_message = (
                f"📅 Thống kê tháng {month}/{year}\n"
                f"----------------------------------\n"
                f"📌 Tổng số món: {total_items}\n"
                f"📌 Tổng số đơn hàng: {total_orders}\n"
                f"📌 Doanh thu tháng: {monthly_revenue:,.0f} VND"
            )

            QMessageBox.information(self, "Thống kê", stats_message)

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể lấy thống kê: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuApp()
    window.show()
    sys.exit(app.exec())
