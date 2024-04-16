from libs.enums.ImportType import ImportType, ImportTypeTranslation
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from libs.ui.PieChartWindow import PieChartWindow
from libs.import_fles import ImportFiles
from PyQt5.uic import loadUi
from libs.db import DB


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('libs/ui/ui_files/main_window.ui', self)
        self._db = DB()

        self.browseFileButton.clicked.connect(self._browse_file)
        self.importButton.clicked.connect(self._import_file)

        self.getSumAction.triggered.connect(self._get_total_cost_plan)
        self.exportPieAction.triggered.connect(self._show_pie)

        for import_type in ImportType:
            self.importType.addItem(ImportTypeTranslation.data[import_type.name], import_type)

    def _browse_file(self):
        """
        Выбрать файл
        """
        file_path = QFileDialog.getOpenFileName(self, 'Выберите файл Excel', '', 'Excel файлы (*.xlsx)')
        if file_path[0]:
            self.filePath.setText(file_path[0])

    def _show_pie(self):
        """
        Отобразить pie диаграмму
        """
        self._db.cursor.callproc('GetCostItemDetails')
        data = self._db.cursor.fetchall()
        self.pieChartWindow = PieChartWindow(data)
        self.pieChartWindow.show()

    def _get_total_cost_plan(self):
        """
        Вывести на экран суммарная себестоимость выпуска изделий на план
        """
        self._db.cursor.callproc('GetTotalCostOfPlan')
        data = self._db.cursor.fetchone()
        total_cost = "{:,.2f}".format(float(data[0])).replace(",", " ")
        QMessageBox.information(self, "Результат", f"Суммарная себестоимость выпуска изделий на план: {total_cost}", QMessageBox.Ok)

    def _import_file(self):
        """
        Импортировать файл
        """
        if not self.filePath.text():
            QMessageBox.warning(self, "Внимание", "Файл не выбран.", QMessageBox.Ok)
            return

        importer = ImportFiles()
        importer.set_settings(self.filePath.text(), self.importType.itemData(self.importType.currentIndex()))
        if importer.import_xls():
            QMessageBox.information(self, "Успех!", "Импорт завершён.", QMessageBox.Ok)
        else:
            QMessageBox.error(self, "Ошибка", "Что-то пошло не так.", QMessageBox.Ok)
