import sys
import mysql
import hashlib
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from loginapp import LoginApp 
import mysql.connector
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)



# Thông tin kết nối MySQL
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "test"

# Kết nối đến cơ sở dữ liệu
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test"
    )

class RegisterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Đăng ký tài khoản")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label_username = QLabel("Tên đăng nhập:")
        self.input_username = QLineEdit()

        self.label_email = QLabel("Email:")
        self.input_email = QLineEdit()

        self.label_password = QLabel("Mật khẩu:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.label_confirm_password = QLabel("Xác nhận mật khẩu:")
        self.input_confirm_password = QLineEdit()
        self.input_confirm_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_register = QPushButton("Đăng ký")
        self.btn_register.clicked.connect(self.register_user)

        self.btn_back = QPushButton("Quay lại đăng nhập")
        self.btn_back.clicked.connect(self.go_to_login)

        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)

        layout.addWidget(self.label_email)
        layout.addWidget(self.input_email)

        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)

        layout.addWidget(self.label_confirm_password)
        layout.addWidget(self.input_confirm_password)

        layout.addWidget(self.btn_register)
        layout.addWidget(self.btn_back)

        self.setLayout(layout)

    def register_user(self):
        username = self.input_username.text().strip()
        email = self.input_email.text().strip()
        password = self.input_password.text().strip()
        confirm_password = self.input_confirm_password.text().strip()

        print(f"📌 Debug: Username = {username}, Email = {email}")  # Kiểm tra đầu vào

        if not username or not email or not password:
            print("⚠️ Thiếu thông tin đăng ký!")
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return

        if password != confirm_password:
            print("⚠️ Mật khẩu không khớp!")
            QMessageBox.warning(self, "Lỗi", "Mật khẩu xác nhận không khớp!")
            return

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        try:
            conn = connect_db()
            if conn is None:
                print("❌ Không thể kết nối MySQL!")
                QMessageBox.critical(self, "Lỗi", "Không thể kết nối cơ sở dữ liệu!")
                return

            cursor = conn.cursor()

            # Kiểm tra username hoặc email đã tồn tại
            cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
            existing_user = cursor.fetchone()

            print(f"🔎 Kiểm tra tài khoản: {existing_user}")  # In ra dữ liệu trả về từ MySQL

            if existing_user:
                print("⚠️ Username hoặc Email đã tồn tại!")
                QMessageBox.warning(self, "Lỗi", "Tên đăng nhập hoặc email đã tồn tại!")
                return

            # Thêm người dùng vào database
            
            sql = "INSERT INTO users (username, password_hash, email, role) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (username, password_hash, email, 'customer'))
            conn.commit()

            print(f"✅ Đăng ký thành công! {cursor.rowcount} dòng đã được thêm.")  # Kiểm tra số dòng được thêm
            if cursor.rowcount == 0:
                print("⚠️ Không có dòng nào được thêm vào database!")

        except mysql.connector.Error as e:
            print(f"❌ Lỗi MySQL: {e}")  # In lỗi ra terminal
            QMessageBox.critical(self, "Lỗi", f"Lỗi MySQL: {e}")


        finally:
            if conn:
                conn.close()
                print("🔌 Đã đóng kết nối MySQL.")



    def go_to_login(self):
        self.login_form = LoginApp()
        self.login_form.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    register_form = RegisterForm()
    register_form.show()
    sys.exit(app.exec())
