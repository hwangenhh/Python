from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFormLayout
from database import Database
import bcrypt

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng ký tài khoản")
        self.setGeometry(300, 200, 350, 250)

        layout = QFormLayout()

        self.input_user = QLineEdit()
        self.input_pass = QLineEdit()
        self.input_confirm_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_confirm_pass.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_register = QPushButton("Đăng ký")
        self.btn_register.clicked.connect(self.register_user)

        layout.addRow(QLabel("Tên đăng nhập:"), self.input_user)
        layout.addRow(QLabel("Mật khẩu:"), self.input_pass)
        layout.addRow(QLabel("Nhập lại mật khẩu:"), self.input_confirm_pass)
        layout.addRow(self.btn_register)

        self.setLayout(layout)

    def register_user(self):
        username = self.input_user.text().strip()
        password = self.input_pass.text().strip()
        confirm_password = self.input_confirm_pass.text().strip()
        print(f"Username: {username}, Password: {password}")
        if not username or not password or not confirm_password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu nhập lại không khớp!")
            return

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        db = Database()
        try:
            db.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password.decode()))
            QMessageBox.information(self, "Thành công", "Đăng ký thành công!")
            self.close()
        except:
            QMessageBox.warning(self, "Lỗi", "Tên đăng nhập đã tồn tại!")
        db.close()
