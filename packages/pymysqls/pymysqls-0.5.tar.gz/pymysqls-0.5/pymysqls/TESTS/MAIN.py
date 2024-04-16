from PyQt5.QtWidgets import QMainWindow, QRadioButton, QCheckBox
from libs.TESTS.TESTW import TESTW  # Import custom TestWidget class from libs package
from PyQt5.uic import loadUi  # Import function to load .ui files
from libs.DB.DB import DB  # Import custom DB class for database interaction


class MAIN(QMainWindow):
    def __init__(self):
        super(MAIN, self).__init__()
        loadUi('libs/OTHER/MAIN.iu', self)  # Load the UI layout from a .ui file
        self._db = DB()  # Initialize database connection

        # Connect button and action signals to the respective slot methods
        self.pushButton.clicked.connect(self._button_clicked)
        self.action.triggered.connect(self._action_clicked)

        # Initialize the UI elements, such as comboBox with items
        self._add_items()

        # Connect another button to add widgets dynamically
        self.addPushButton.clicked.connect(self._add_widget)

    def _add_widget(self):
        """Creates and adds a new TestWidget to the specified layout."""
        test_widget = TESTW()
        self.testWidgerLayout.addWidget(test_widget)  # Add custom widget to layout

    def _action_clicked(self):
        """Triggers the same functionality as the push button when the action is triggered."""
        self._button_clicked()

    def _button_clicked(self):
        """Handles button click events by updating UI elements based on user input and interactions."""
        # Update the titles of groupBoxes based on the checked radio button in each group
        for radiobutton in self.groupBox.findChildren(QRadioButton):
            if radiobutton.isChecked():
                self.groupBox.setTitle(radiobutton.text())

        for radiobutton in self.groupBox2.findChildren(QRadioButton):
            if radiobutton.isChecked():
                self.groupBox2.setTitle(radiobutton.text())

        # Collect and display checked items in groupBox3
        list = []
        for check_box in self.groupBox3.findChildren(QCheckBox):
            if check_box.isChecked():
                list.append(check_box.text())
        self.groupBox3.setTitle(", ".join(list))

        # Update labels with text from a line edit and the current index or data of a combo box
        self.label.setText(self.lineEdit.text())
        self.label2.setText(f"{self.comboBox.currentIndex()}")
        self.label3.setText(f"{self.comboBox.currentData()}")

        # Update progress bar based on the current index of the combo box
        self.progressBar.setValue(self.comboBox.currentIndex() * 20)

    def _add_items(self):
        """Populates the comboBox with items and associated user data."""
        for i in range(6):
            self.comboBox.addItem(f"{i}", f"{i}-userdata")  # Add items with a loop, assigning user data to each item
