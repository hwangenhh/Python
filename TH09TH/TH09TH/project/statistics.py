from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from database import Database

class Statistics(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thống kê sản phẩm")
        self.setGeometry(300, 300, 500, 400)

        layout = QVBoxLayout()
        self.canvas = FigureCanvas(self.create_chart())

        layout.addWidget(QLabel("Biểu đồ số lượng sản phẩm theo danh mục"))
        layout.addWidget(self.canvas)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def create_chart(self):
        db = Database()
        data = db.query("SELECT cat_id, COUNT(*) FROM products GROUP BY cat_id")
        db.close()

        categories = [row[0] for row in data]
        counts = [row[1] for row in data]

        fig, ax = plt.subplots()
        ax.bar(categories, counts)
        ax.set_xlabel("Danh mục")
        ax.set_ylabel("Số lượng sản phẩm")
        ax.set_title("Thống kê sản phẩm")

        return fig

if __name__ == "__main__":
    app = QApplication([])
    window = Statistics()
    window.show()
    app.exec()
