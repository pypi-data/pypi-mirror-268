from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtWidgets import QFileDialog
import matplotlib.pyplot as plt


class PieChartWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("Доля каждой статьи затрат в общей себестоимости выпуска")

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        self.layout.addWidget(self.canvas)
        self.plot(data)

        self.saveButton = QPushButton("Сохранить изображение")
        self.saveButton.clicked.connect(self.save_plot)
        self.layout.addWidget(self.saveButton)

    def plot(self, data):
        labels = [x[0] for x in data]
        sizes = [x[1] for x in data]

        ax = self.figure.add_subplot(111)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')
        self.canvas.draw()

    def save_plot(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Сохранить изображение", "", "PNG Files (*.png);;All Files (*)",
                                                  options=options)
        if fileName:
            self.figure.savefig(fileName)
