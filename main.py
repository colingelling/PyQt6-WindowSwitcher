from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):

    # Each button used for navigation is bound to its own signal in order to switch between multiple windows from one
    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # setup ui
        from ui.MainWindow import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # load window context and finalized content
        self.window_properties()
        self.window_content()

    def window_properties(self):
        self.setWindowTitle('MainWindow (1)')

    def window_content(self):

        # Create navigation buttons for switching between multiple windows
        first_window_button = QAction('Home', self)
        second_window_button = QAction('Second window', self)
        third_window_button = QAction('Third window', self)

        # Each button refers to an individual signal
        first_window_button.triggered.connect(self.switch_first_window)
        second_window_button.triggered.connect(self.switch_second_window)
        third_window_button.triggered.connect(self.switch_third_window)

        # Add each button into the menubar on the top of every window
        self.ui.menubar.addAction(first_window_button)
        self.ui.menubar.addAction(second_window_button)
        self.ui.menubar.addAction(third_window_button)

    # Use the signals for every button individually
    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()


class SecondWindow(QMainWindow):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # ui
        from ui.MainWindow import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.window_properties()
        self.window_content()

    def window_properties(self):
        self.setWindowTitle('Window (2)')

    def window_content(self):
        first_window_button = QAction('Home', self)
        second_window_button = QAction('Second window', self)
        third_window_button = QAction('Third window', self)

        first_window_button.triggered.connect(self.switch_first_window)
        second_window_button.triggered.connect(self.switch_second_window)
        third_window_button.triggered.connect(self.switch_third_window)

        self.ui.menubar.addAction(first_window_button)
        self.ui.menubar.addAction(second_window_button)
        self.ui.menubar.addAction(third_window_button)

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()


class ThirdWindow(QMainWindow):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # ui
        from ui.MainWindow import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.window_properties()
        self.window_content()

    def window_properties(self):
        self.setWindowTitle('Window (3)')

    def window_content(self):
        first_window_button = QAction('Home', self)
        second_window_button = QAction('Second window', self)
        third_window_button = QAction('Third window', self)

        first_window_button.triggered.connect(self.switch_first_window)
        second_window_button.triggered.connect(self.switch_second_window)
        third_window_button.triggered.connect(self.switch_third_window)

        self.ui.menubar.addAction(first_window_button)
        self.ui.menubar.addAction(second_window_button)
        self.ui.menubar.addAction(third_window_button)

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()


class Controller:

    def __init__(self):
        pass

    # Instantiate the window Classes per method from now on, bind the windows to individual signals and show the window

    def show_main_window(self):
        self.window = MainWindow()
        self.window.switch_second.connect(self.show_second_window)
        self.window.switch_third.connect(self.show_third_window)
        self.window.show()

    def show_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.switch_first.connect(self.show_main_window)
        self.second_window.switch_third.connect(self.show_third_window)
        self.window.close()
        self.second_window.show()

    def show_third_window(self):
        self.second_window = ThirdWindow()
        self.second_window.switch_first.connect(self.show_main_window)
        self.second_window.switch_second.connect(self.show_second_window)
        self.second_window.close()
        self.second_window.show()


# Create the main application, initialize and build
def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main_window()
    sys.exit(app.exec())


# Instantiate the application
if __name__ == '__main__':
    import sys
    main()
