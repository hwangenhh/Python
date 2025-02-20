from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import sys
import mysql.connector
import hashlib

class RegisterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Đăng ký tài khoản")
        self.setGeometry(100, 100, 300, 250)

        layout = QVBoxLayout()

        # Nhãn và ô nhập
        self.label_username = QLabel("Tên người dùng:")
        self.input_username = QLineEdit()
        self.label_email = QLabel("Email:")
        self.input_email = QLineEdit()
        self.label_password = QLabel("Mật khẩu:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        # Nút đăng ký
        self.btn_register = QPushButton("Đăng ký")
        self.btn_register.clicked.connect(self.register_user)

        # Thêm vào layout
        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_email)
        layout.addWidget(self.input_email)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.btn_register)

        self.setLayout(layout)

    def register_user(self):
        username = self.input_username.text()
        email = self.input_email.text()
        password = self.input_password.text()

        if not username or not email or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Kết nối MySQL (Thay đổi thông tin theo database của bạn)
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="menu_app"
            )
            cursor = conn.cursor()

            # Kiểm tra xem email đã tồn tại chưa
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Lỗi", "Email này đã được đăng ký!")
                conn.close()
                return

            # Mã hóa mật khẩu
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Chèn dữ liệu vào database
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                           (username, email, hashed_password))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Thành công", "Đăng ký tài khoản thành công!\nBạn có thể đăng nhập ngay.")
            self.input_username.clear()
            self.input_email.clear()
            self.input_password.clear()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối CSDL: {err}")

        print(f"Đăng ký: {username}, {email}, {password}")  # Kiểm tra dữ liệu đầu vào
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        result = cursor.fetchall()
        print(f"User trong DB: {result}")  # Kiểm tra MySQL có lưu dữ liệu không




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterForm()
    window.show()
    sys.exit(app.exec())
           
