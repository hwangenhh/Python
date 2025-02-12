from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget
from database import Database

class ProductMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý sản phẩm")
        self.setGeometry(250, 250, 400, 300)

        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        self.load_products()

        self.btn_add = QPushButton("Thêm sản phẩm")
        self.btn_edit = QPushButton("Sửa sản phẩm")
        self.btn_delete = QPushButton("Xóa sản phẩm")

        layout.addWidget(QLabel("Danh sách sản phẩm:"))
        layout.addWidget(self.list_widget)
        layout.addWidget(self.btn_add)
        layout.addWidget(self.btn_edit)
        layout.addWidget(self.btn_delete)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_products(self):
        db = Database()
        products = db.query("SELECT name FROM products")
        db.close()
        
        for product in products:
            self.list_widget.addItem(product[0])

if __name__ == "__main__":
    app = QApplication([])
    window = ProductMenu()
    window.show()
    app.exec()
