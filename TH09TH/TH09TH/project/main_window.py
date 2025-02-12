from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trang chủ")
        self.setGeometry(300, 200, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Chào mừng bạn đến với hệ thống!")
        self.btn_logout = QPushButton("Đăng xuất")
        self.btn_logout.clicked.connect(self.logout)

        layout.addWidget(self.label)
        layout.addWidget(self.btn_logout)

        self.setLayout(layout)

    def logout(self):
        self.close()
