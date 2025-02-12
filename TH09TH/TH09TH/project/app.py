from PyQt6.QtWidgets import QApplication
from login import LoginWindow
from main_window import MainWindow  # Import cửa sổ chính
from menu import ProductMenu  # Import cửa sổ chính

if __name__ == "__main__":
    app = QApplication([])
    menu = ProductMenu()
    menu.show()
    app.exec()
