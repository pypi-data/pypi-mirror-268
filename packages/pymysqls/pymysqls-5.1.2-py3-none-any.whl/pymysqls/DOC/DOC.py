class DOC:
    def __init__(self):
        print("")

    def imports_mw(self):
        """
        from PyQt5.QtWidgets import QMainWindow, QRadioButton, QCheckBox
        from libs.TESTS.TESTW import TESTW
        from PyQt5.uic import loadUi
        from libs.DB.DB import DB
        """
        return

    def mw_class(self):
        """
        class MainWindow(QMainWindow):
            def __init__(self):
                super(MainWindow, self).__init__()
                loadUi('libs/ui/main_windows.ui', self)
                self._db = DB()
        """
        return

    def push_button_click(self):
        """self.pushButton.clicked.connect(self._button_clicked)"""
        return

    def action_click(self):
        """self.action.triggered.connect(self._action_clicked)"""
        return

    def show_error(self):
        """QMessageBox.critical(None, "Error", "Error!")"""
        return

    def show_warning(self):
        """QMessageBox.warning(None, "Warning", "Warning!")"""
        return

    def show_information(self):
        """QMessageBox.information(None, "Information", "Information!")"""
        return

    def confirm_action(self):
        """
        result = QMessageBox.question(None, "Confirm", "Are u sure?",
                                      QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            print("Yes...")
        else:
            print("No.")
        """
        return

    def add_widget(self):
        """
        test_widget = TestWidget()
        self.testWidgetLayout.addWidget(test_widget)
        """
        return

    def get_group_box_checked(self):
        """
        for radiobutton in self.groupBox.findChildren(QRadioButton):
            if radiobutton.isChecked():
                self.groupBox.setTitle(radiobutton.text())
        """
        return

    def get_check_box_checked(self):
        """
        list = []
        for check_box in self.groupBox3.findChildren(QCheckBox):
            if check_box.isChecked():
                list.append(check_box.text())
        self.groupBox3.setTitle(", ".join(list))
        """
        return

    def combobox_current_index_data(self):
        """
        self.label.setText(f"{self.comboBox.currentIndex()}")
        self.label.setText(f"{self.comboBox.currentData()}")
        """
        return

    def set_progress_bar_value(self):
        """
        self.progressBar.setValue(20)
        """
        return

    def add_combobox_items(self):
        """
        for i in range(6):
            self.comboBox.addItem(f"{i}", f"{i}-userdata")
        """

    def imports_testw(self):
        """
        from PyQt5.QtWidgets import QWidget
        from PyQt5.uic import loadUi
        """
        return

    def testw_class(self):
        """
        class TESTW(QWidget):
            def __init__(self):
                super(TESTW, self).__init__()
                loadUi('libs/ui/widget_test.ui', self)
        """
        return

    def imports_db(self):
        """import pymysql"""
        return

    def db_class(self):
        """
        class DB:
            def __init__(self):
                self.cursor = None
                self.connection = None
                self.connect()
        """
        return

    def db_connect(self):
        """
        def connect(self):
            self.connection = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="main", charset="utf8")
            self.cursor = self.connection.cursor()
        """
        return

    def db_get(self):
        """
        def get(self, name, table):
            self.cursor.execute(f"SELECT * FROM `{table}` WHERE `name` = '{name}';")
            return self.cursor.fetchone()
        """
        return

    def db_insert(self):
        """
        def insert(self, table, into, values):
            self.cursor.execute(f"INSERT INTO `{table}`({','.join(into)}) VALUES ({','.join(values)})")
            self.connection.commit()
        """
        return

    def db_del(self):
        """
        def __del__(self):
            self.cursor.close()
            self.connection.close()
        """
        return

    def imports_st(self):
        """
        from libs.ui.MainWindow import MainWindow
        from PyQt5 import QtWidgets
        import sys
        """
        return

    def st_base(self):
        """
        if __name__ == "__main__":
            app = QtWidgets.QApplication([])
            window = MAIN()
            window.show()
            sys.exit(app.exec())
        """
        return
