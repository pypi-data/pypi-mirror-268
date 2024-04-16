from lib.db import DB
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from Ui_Form import Ui_Form


class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.db = DB()
        self.render_data()

    def get_data(self):
        if self.db.con:
            try:
                cursor = self.db.con.cursor()
                query = f"SELECT service.name, service.price, data, status, service.img FROM orders LEFT JOIN service ON orders.id_service = service.id;"
                cursor.execute(query)
                data = cursor.fetchall()
                return data
            except Exception as e:
                print("Ошибка при выполнении запроса:", e)
                return []
        else:
            return []

    def render_data(self):
        data = self.get_data()
        for row in data:
            self.add_object(row)

    def add_object(self, data):
        obj = QtWidgets.QHBoxLayout()
        image = QtWidgets.QLabel()
        image.setMinimumSize(QtCore.QSize(150, 150))
        image.setMaximumSize(QtCore.QSize(150, 150))
        if data[4] != "":
            pixmap = QPixmap()
            pixmap.loadFromData(data[4])
            image.setPixmap(pixmap)
        image.setScaledContents(True)
        obj.addWidget(image)
        label = QtWidgets.QLabel()
        label.setText(f"{data[0]}\n{data[1]} руб.\n{data[2].strftime('%H:%M:%S %d.%m.%y')}\nСтатус: {data[3]}")
        obj.addWidget(label)
        self.verticalLayout.addLayout(obj)


# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
