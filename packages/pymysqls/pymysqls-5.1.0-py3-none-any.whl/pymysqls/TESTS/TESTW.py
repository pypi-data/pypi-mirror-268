from PyQt5.QtWidgets import QWidget  # Import the base QWidget for creating custom widgets
from PyQt5.uic import loadUi  # Import function to load .ui files for the UI design


class TESTW(QWidget):
    """
    TestWidget is a custom widget class that extends QWidget.
    It loads its user interface from a .ui file, making it reusable
    and easy to manage in different parts of a PyQt application.
    """

    def __init__(self):
        """
        Initializes the TestWidget instance by loading the predefined
        user interface layout from a .iu file.
        """
        super(TESTW, self).__init__()  # Initialize the parent QWidget class
        loadUi('libs/OTHER/TESTW.iu', self)  # Load the IU layout from the specified .ui file located in libs folder
