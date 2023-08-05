import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize


class ExampleWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(320, 240))
        self.setWindowTitle('Example')

        central_widget = QWidget(self)
        grid_layout = QGridLayout(central_widget)
        self.setCentralWidget(central_widget)

        self._label = QLabel('', self)
        self._label.setAlignment(QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self._label, 0, 0)

        self._counter = 0

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            self._counter += 1
            self._label.setText('Клавиша Q нажата {} раз'.format(self._counter))
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = ExampleWindow()
    main_window.show()
    sys.exit(app.exec_())