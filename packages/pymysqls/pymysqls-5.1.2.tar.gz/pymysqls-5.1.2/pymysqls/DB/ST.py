from libs.TESTS.MAIN import MAIN  # Import MAIN class from the library module located under libs/TESTS
from PyQt5 import QtWidgets  # Import QtWidgets module for GUI components
import sys  # Import sys to interact with the interpreter

if __name__ == "__main__":
    """
    This block checks if the script is run as the main module and not imported as a module.
    It is the entry point for the Python script when it is executed as the main program.
    """

    app = QtWidgets.QApplication([])  # Create an instance of QApplication for managing GUI application lifecycle
    window = MAIN()  # Create an instance of the MAIN class, which should define a main window or similar widget
    window.show()  # Display the main window to the user

    sys.exit(
        app.exec())  # Start the main event loop of the application and exit the script with the status code returned by app.exec()
