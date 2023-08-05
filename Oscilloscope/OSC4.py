import sys
import numpy as np
import random
from PyQt5 import QtCore, QtWidgets, uic

import matplotlib
matplotlib.use('QT5Agg')

import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

flag1 = 0
limX = 100
period = 10

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('test.ui', self)
        # self.flag_1 = 0
        self.fig, self.ax1 = plt.subplots()

        self.n_data = limX
        self.xdata = list(range(self.n_data))
        self.ydata = [random.randint(0, 10) for i in range(self.n_data)]
        self.zdata = [random.randint(0, 10) for i in range(self.n_data)]
        self._line1, = self.ax1.plot(self.xdata, self.ydata, "r")
        self._line2, = self.ax1.plot(self.xdata, self.zdata, "g")

        self.plotWidget = FigureCanvas(self.fig)
        lay = QtWidgets.QVBoxLayout(self.content_plot)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.plotWidget)
        # add toolbar
        self.addToolBar(QtCore.Qt.TopToolBarArea, NavigationToolbar(self.plotWidget, self))

        self._timer = self.plotWidget.new_timer(period)
        self._timer.add_callback(self._update_canvas)
        self._timer.start()

    def _update_canvas(self):
        if flag1:
            self.ydata = self.ydata[1:] + [random.randint(0, 10)]
            self.zdata = self.zdata[1:] + [random.randint(0, 10)]
            self._line1.set_data(self.xdata, self.ydata)
            self._line1.figure.canvas.draw()
            self._line2.set_data(self.xdata, self.zdata)
            self._line2.figure.canvas.draw()
            # print('UP')

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()

    def start_stop():
        global flag1
        if flag1:
            flag1 = 0
        else:
            flag1 = 1

    def updateSLD1():
        window.LCD1.display(window.SLD1.value())
        global limX
        limX = window.SLD1.value()

    def updateSLD2():
        window.LCD2.display(window.SLD2.value())
        global period
        period = window.SLD2.value()

    window.BTN1.clicked.connect(start_stop)
    window.SLD1.valueChanged.connect(updateSLD1)
    window.SLD2.valueChanged.connect(updateSLD2)
    window.show()
    sys.exit(app.exec_())
