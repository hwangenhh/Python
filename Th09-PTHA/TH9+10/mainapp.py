import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLineEdit, QMessageBox, QPushButton, QComboBox, QInputDialog
from PyQt6.uic import loadUi
from datetime import datetime


class MenuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            loadUi("D:\\Python\\Th09-PTHA\\TH09_TrangTTH\\main_ui.ui", self)
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể tải file UI: {str(e)}")
            sys.exit(1)
        
        

        try:
            # Lấy các widget từ UI
            self.txtID = self.findChild(QLineEdit, "txtID")
            self.txtName = self.findChild(QLineEdit, "txtTen")
            self.txtDescription = self.findChild(QLineEdit, "txtMoTa")
            self.txtPrice = self.findChild(QLineEdit, "txtGia")
            self.txtCategory = self.findChild(QLineEdit, "txtLoai")
            self.txtStatus = self.findChild(QLineEdit, "txtTrangThai")
            self.btnAdd = self.findChild(QPushButton, "btnAdd")
            self.btnEdit = self.findChild(QPushButton, "btnEdit")
            self.btnDelete = self.findChild(QPushButton, "btnDelete")
            self.btnRefresh = self.findChild(QPushButton, "btnRefresh")
            self.btnStatistics = self.findChild(QPushButton, "btnStatistics")
            self.btnPay = self.findChild(QPushButton, "btnPay")
            self.btnConfirmPayment = self.findChild(QComboBox, "btnConfirmPayment")

            # Kiểm tra xem các widget có tồn tại không
            widgets = [self.txtID, self.txtName, self.txtDescription, self.txtPrice, 
                      self.txtCategory, self.txtStatus, self.btnAdd, self.btnEdit, 
                      self.btnDelete, self.btnRefresh, self.btnStatistics, self.btnPay, 
                      self.btnConfirmPayment]
            
            for widget in widgets:
                if widget is None:
                    raise Exception(f"Không tìm thấy widget {widget}")

            # Thiết lập ID chỉ đọc
            self.txtID.setReadOnly(True)

            # Kết nối sự kiện
            self.btnAdd.clicked.connect(self.add_menu)
            self.btnEdit.clicked.connect(self.edit_menu)
            self.btnDelete.clicked.connect(self.delete_menu)
            self.btnRefresh.clicked.connect(self.reset_form)
            self.btnStatistics.clicked.connect(self.show_statistics)
            self.btnPay.clicked.connect(self.process_payment)
        
            # Thêm các phương thức thanh toán vào ComboBox
            self.btnConfirmPayment.addItems(["Tiền mặt", "Chuyển khoản", "Quẹt thẻ"])

            # Kết nối với cơ sở dữ liệu và load dữ liệu

            self.test_db_connection()
            self.load_data()

        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi khởi tạo ứng dụng: {str(e)}")
            sys.exit(1)

    def test_db_connection(self):
        """Kiểm tra kết nối database"""
        try:
            db = self.connect_db()
            db.close()
        except Exception as e:
            QMessageBox.critical(self, "Lỗi Database", 
                               f"Không thể kết nối đến cơ sở dữ liệu: {str(e)}\n"
                               "Vui lòng kiểm tra:\n"
                               "1. MySQL đã được cài đặt và đang chạy\n"
                               "2. Database 'test' đã được tạo\n"
                               "3. Bảng 'menu' đã được tạo\n"
                               "4. Thông tin kết nối (user, password) là chính xác")
            raise

    def connect_db(self):
        """Kết nối MySQL"""
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="test"
            )
        except mysql.connector.Error as e:
            raise Exception(f"Lỗi kết nối MySQL: {str(e)}")

    def validate_input(self, price, status):
        """Kiểm tra dữ liệu đầu vào"""
        try:
            price_val = float(price)
            if price_val <= 0:
                raise ValueError("Giá phải lớn hơn 0")
            
            status_val = int(status)
            if status_val not in [0, 1]:
                raise ValueError("Trạng thái phải là 0 hoặc 1")
                
            return price_val, status_val
        except ValueError as e:
            raise ValueError(f"Dữ liệu không hợp lệ: {str(e)}")


    def load_data(self):
        """Load dữ liệu từ MySQL vào bảng tableMenu"""
        try:
            db = self.connect_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM menu")
            rows = cursor.fetchall()

            self.tableMenu.setRowCount(len(rows))
            for row_idx, row_data in enumerate(rows):
                for col_idx, value in enumerate(row_data):
                    self.tableMenu.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tải dữ liệu: {str(e)}")
        finally:
            if 'db' in locals():
                db.close()
    def add_menu(self):
        """Thêm món mới từ dữ liệu nhập"""
        try:
            # Lấy dữ liệu từ form
            name = self.txtName.text().strip()
            description = self.txtDescription.text().strip()
            price = self.txtPrice.text().strip()
            category = self.txtCategory.text().strip()
            status = self.txtStatus.text().strip()

            # Kiểm tra dữ liệu trống
            if not all([name, description, price, category, status]):
                raise ValueError("Vui lòng nhập đầy đủ thông tin!")

            # Validate dữ liệu
            price_val, status_val = self.validate_input(price, status)

            # Thêm vào database
            db = self.connect_db()
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO menu (name, description, price, category, availability) 
                VALUES (%s, %s, %s, %s, %s)
            """, (name, description, price_val, category, status_val))
            db.commit()
            
            QMessageBox.information(self, "Thành công", "Đã thêm món mới!")
            self.load_data()
            self.reset_form()

        except ValueError as e:
            QMessageBox.warning(self, "Lỗi", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể thêm món: {str(e)}")
        finally:
            if 'db' in locals():
                db.close()

    def edit_menu(self):
        """Chỉnh sửa mục đã chọn"""
        row = self.tableMenu.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một mục để sửa!")
            return

        menu_id = self.tableMenu.item(row, 0).text()
        name = self.txtName.text()
        description = self.txtDescription.text()
        price = self.txtPrice.text()
        category = self.txtCategory.text()
        status = self.txtStatus.text()

        try:
            db = self.connect_db()
            cursor = db.cursor()
            cursor.execute("UPDATE menu SET name=%s, description=%s, price=%s, category=%s, availability=%s WHERE menu_id=%s",
                        (name, description, float(price), category, int(status), menu_id))
            db.commit()
            db.close()
            self.load_data()
            self.reset_form()
            QMessageBox.information(self, "Thành công", "Đã cập nhật món!")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể cập nhật: {str(e)}")

    def delete_menu(self):
        """Xóa mục đã chọn"""
        row = self.tableMenu.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một mục để xóa!")
            return

        reply = QMessageBox.question(self, "Xác nhận", "Bạn có chắc muốn xóa món này?",
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                menu_id = self.tableMenu.item(row, 0).text()
                db = self.connect_db()
                cursor = db.cursor()
                cursor.execute("DELETE FROM menu WHERE menu_id=%s", (menu_id,))
                db.commit()
                db.close()
                self.load_data()
                self.reset_form()
                QMessageBox.information(self, "Thành công", "Đã xóa món!")
            except Exception as e:
                QMessageBox.critical(self, "Lỗi", f"Không thể xóa: {str(e)}")

    def reset_form(self):
        """Xóa trắng toàn bộ các ô nhập liệu"""
        self.txtID.clear()
        self.txtName.clear()
        self.txtDescription.clear()
        self.txtPrice.clear()
        self.txtCategory.clear()
        self.txtStatus.clear()

    
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
    
    def process_payment(self):
        """Xử lý thanh toán các món đã chọn"""
        rows = self.tableMenu.selectionModel().selectedRows()  # Lấy các dòng được chọn
        if not rows:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn ít nhất một món để thanh toán!")
            return

        payment_method = self.btnConfirmPayment.currentText()
        if not payment_method:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn phương thức thanh toán!")
            return

        try:
            total_amount = 0
            selected_items = []

            for row in rows:
                menu_id = self.tableMenu.item(row.row(), 0).text()  # Lấy ID món
                name = self.tableMenu.item(row.row(), 1).text()  # Lấy tên món
                price = float(self.tableMenu.item(row.row(), 3).text())  # Lấy giá

                total_amount += price
                selected_items.append((menu_id, name, price))

            # Hiển thị tổng tiền và xác nhận thanh toán
            item_details = "\n".join([f"{name}: {price:,.0f} VND" for _, name, price in selected_items])
            confirm_message = (
                f"Các món đã chọn:\n{item_details}\n\n"
                f"Phương thức thanh toán: {payment_method}\n"
                f"Tổng tiền: {total_amount:,.0f} VND\n\n"
                "Bạn có chắc chắn muốn thanh toán không?"
            )

            reply = QMessageBox.question(self, "Xác nhận thanh toán", confirm_message,
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                self.complete_payment(selected_items, total_amount, payment_method)  # GỌI ĐÚNG CÁCH

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi xử lý thanh toán: {str(e)}")

            """Xử lý thanh toán các món đã chọn"""
            rows = self.tableMenu.selectionModel().selectedRows()  # Lấy các dòng được chọn
            if not rows:
                QMessageBox.warning(self, "Lỗi", "Vui lòng chọn ít nhất một món để thanh toán!")
                return

            payment_method = self.btnConfirmPayment.currentText()
            if not payment_method:
                QMessageBox.warning(self, "Lỗi", "Vui lòng chọn phương thức thanh toán!")
                return

            try:
                total_amount = 0
                selected_items = []

                for row in rows:
                    menu_id = self.tableMenu.item(row.row(), 0).text()  # Lấy ID món
                    name = self.tableMenu.item(row.row(), 1).text()  # Lấy tên món
                    price = float(self.tableMenu.item(row.row(), 3).text())  # Lấy giá

                    total_amount += price
                    selected_items.append((menu_id, name, price))

                # Hiển thị tổng tiền và xác nhận thanh toán
                item_details = "\n".join([f"{name}: {price:,.0f} VND" for _, name, price in selected_items])
                confirm_message = (
                    f"Các món đã chọn:\n{item_details}\n\n"
                    f"Phương thức thanh toán: {payment_method}\n"
                    f"Tổng tiền: {total_amount:,.0f} VND\n\n"
                    "Bạn có chắc chắn muốn thanh toán không?"
                )

                reply = QMessageBox.question(self, "Xác nhận thanh toán", confirm_message,
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

                if reply == QMessageBox.StandardButton.Yes:
                    self.complete_payment(selected_items, total_amount, payment_method)
            except Exception as e:
                QMessageBox.critical(self, "Lỗi", f"Lỗi xử lý thanh toán: {str(e)}")

    def complete_payment(self, selected_items, total_amount, payment_method):
        """Hoàn tất thanh toán, cập nhật trạng thái món và lưu giao dịch"""
        try:
            db = self.connect_db()
            cursor = db.cursor()

            # Lấy ngày giờ hiện tại
            order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Lưu thông tin vào bảng orders (bỏ order_id vì là AUTO_INCREMENT)
            cursor.execute(
                "INSERT INTO orders (total_amount, order_date) VALUES (%s, %s)",
                (total_amount, order_date)
            )

            order_id = cursor.lastrowid  # Lấy ID đơn hàng vừa thêm vào

            # Lưu từng món vào bảng order_details
            for menu_id, _, price in selected_items:
                cursor.execute("INSERT INTO order_details (order_id, menu_id, price) VALUES (%s, %s, %s)", 
                            (order_id, menu_id, price))
                # Kiểm tra trạng thái món trước khi cập nhật
                cursor.execute("SELECT availability FROM menu WHERE menu_id = %s", (menu_id,))
                availability = cursor.fetchone()[0]
                if availability == 1:
                    cursor.execute("UPDATE menu SET availability = 0 WHERE menu_id = %s", (menu_id,))

            db.commit()
            db.close()

            QMessageBox.information(self, "Thanh toán thành công",
                                    f"Thanh toán {len(selected_items)} món thành công!\n"
                                    f"Tổng số tiền: {total_amount:,.0f} VND\n"
                                    f"Phương thức: {payment_method}")

            # Load lại dữ liệu để cập nhật trạng thái món
            self.load_data()

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể hoàn tất thanh toán: {str(e)}")


    def handle_cash_payment(self):
        QMessageBox.information(self, "Thanh toán tiền mặt", "Vui lòng thu tiền mặt từ khách hàng.")
        self.complete_payment()  # Đảm bảo phương thức này có tồn tại

    def handle_bank_transfer(self):
        bank_info = "Số tài khoản: 123456789\nNgân hàng: ABC Bank\nChủ tài khoản: Công ty XYZ"
        QMessageBox.information(self, "Thông tin chuyển khoản", f"Thông tin tài khoản:\n\n{bank_info}")
        self.complete_payment()  # Gọi sau khi hiển thị thông tin

    def handle_card_payment(self):
        QMessageBox.information(self, "Thanh toán thẻ", "Vui lòng quẹt thẻ của khách hàng.")
        self.complete_payment()  # Gọi sau khi quẹt thẻ
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuApp()
    window.show()
    sys.exit(app.exec())