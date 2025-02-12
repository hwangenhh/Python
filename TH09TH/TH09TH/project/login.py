from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFormLayout
from database import Database
import bcrypt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng nhập")
        self.setGeometry(300, 200, 350, 200)

        layout = QFormLayout()

        self.input_user = QLineEdit()
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_login = QPushButton("Đăng nhập")
        self.btn_register = QPushButton("Chưa có tài khoản? Đăng ký")
        
        self.btn_login.clicked.connect(self.login_user)
        self.btn_register.clicked.connect(self.open_register_window)

        layout.addRow(QLabel("Tên đăng nhập:"), self.input_user)
        layout.addRow(QLabel("Mật khẩu:"), self.input_pass)
        layout.addRow(self.btn_login)
        layout.addRow(self.btn_register)

        self.setLayout(layout)

    def login_user(self):
        username = self.input_user.text().strip()
        password = self.input_pass.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        db = Database()
        user = db.fetch_one("SELECT password FROM users WHERE username = %s", (username,))
        db.close()

        if user and bcrypt.checkpw(password.encode(), user[0].encode()):
            QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")
            self.close()
            self.open_main_window()
        else:
            QMessageBox.warning(self, "Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")

    def open_register_window(self):
        from register import RegisterWindow
        self.register_win = RegisterWindow()
        self.register_win.show()

    def open_main_window(self):
        from main_window import MainWindow
        self.main_win = MainWindow()
        self.main_win.show()
