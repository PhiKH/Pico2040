from PyQt5 import QtWidgets, uic
import random
from PyQt5 import QtCore, QtWidgets
import numpy as np
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import sys
import time


from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvas()                  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)


if __name__ == '__main__':
    print("Start")
    APP = QtWidgets.QApplication([])
    UI = uic.loadUi("window_4.ui")

    #
    # class ApplicationWindow(UI.Plot_widget):
    #     def __init__(self):
    #         super().__init__()
    #         self._main = QtWidgets.QWidget()
    #         self.setCentralWidget(self._main)
    #         layout = QtWidgets.QVBoxLayout(self._main)
    #
    #         static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
    #         # Ideally one would use self.addToolBar here, but it is slightly
    #         # incompatible between PyQt6 and other bindings, so we just add the
    #         # toolbar as a plain widget instead.
    #         layout.addWidget(NavigationToolbar(static_canvas, self))
    #         layout.addWidget(static_canvas)
    #
    #         dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
    #         layout.addWidget(dynamic_canvas)
    #         layout.addWidget(NavigationToolbar(dynamic_canvas, self))
    #
    #         self._static_ax = static_canvas.figure.subplots()
    #         t = np.linspace(0, 10, 501)
    #         self._static_ax.plot(t, np.tan(t), ".")
    #
    #         self._dynamic_ax = dynamic_canvas.figure.subplots()
    #         t = np.linspace(0, 10, 101)
    #         # Set up a Line2D.
    #         self._line, = self._dynamic_ax.plot(t, np.sin(t + time.time()))
    #         self._timer = dynamic_canvas.new_timer(50)
    #         self._timer.add_callback(self._update_canvas)
    #         self._timer.start()
    #
    #     def _update_canvas(self):
    #         t = np.linspace(0, 10, 101)
    #         # Shift the sinusoid as a function of time.
    #         self._line.set_data(t, np.sin(t + time.time()))
    #         self._line.figure.canvas.draw()
    #
    # # qapp = QtWidgets.QApplication.instance()
    # # if not qapp:
    # #     qapp = QtWidgets.QApplication(sys.argv)
    # app = ApplicationWindow()
    # app.show()
    # app.activateWindow()
    # app.raise_()
    # qapp.exec()
    # UI.Plot_widget = ApplicationWindow()
    UI.show()
    # UI.activateWindow()
    # UI.raise_()
APP.exec()

    # layout = QtWidgets.QVBoxLayout(UI.Plot_widget)
    #
    # # static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
    # #
    # # layout.addWidget(NavigationToolbar(static_canvas, UI.Plot_widget))
    # # layout.addWidget(static_canvas)
    # # UI.Plot_widget._static_ax = static_canvas.figure.subplots()
    #
    # dynamic_canvas = FigureCanvas(Figure())
    # layout.addWidget(NavigationToolbar(dynamic_canvas, UI.Plot_widget))
    # layout.addWidget(dynamic_canvas)
    #
    # UI.Plot_widget._dynamic_ax = dynamic_canvas.figure.subplots()
    # # t = np.linspace(0, 10, 101)
    # # Set up a Line2D.
    #
    # # def update_plot(self):
    # #     t = np.linspace(0, 10, 101)
    # #     # Shift the sinusoid as a function of time.
    # #     UI.Plot_widget._line.set_data(t, np.sin(t + time.time()))
    # #     UI.Plot_widget._line.figure.canvas.draw()
    # #     print('UP')
    # #
    # # UI.Plot_widget._line, = UI.Plot_widget._dynamic_ax.plot(t, np.sin(t + time.time()))
    # #
    # # timer = QtCore.QTimer()
    # # timer.setInterval(100)
    # # timer.timeout.connect(update_plot)
    # # timer.start()
    #
    #
    # n_data = 10
    # xdata = list(range(n_data))
    # ydata = [random.randint(0, 10) for i in range(n_data)]
    #
    # print(xdata)
    # print(ydata)
    # # UI.Plot_widget._static_ax.plot(xdata, ydata, "r")
    # UI.Plot_widget._line, = UI.Plot_widget._dynamic_ax.plot(xdata, ydata)
    # timer = dynamic_canvas.new_timer(50)
    # timer.add_callback(_update_canvas(UI.Plot_widget))
    # timer.start()

    # UI.show()

    # def update_plot(self):
    #     # Drop off the first y element, append a new one.
    #     ydata = ydata[1:] + [random.randint(0, 10)]
    #     # zdata = self.zdata[1:] + [random.randint(0, 10)]
    #     # Note: we no longer need to clear the axis.
    #     if self._plot_ref is None:
    #         # First time we have no plot reference, so do a normal plot.
    #         # .plot returns a list of line <reference>s, as we're
    #         # only getting one we can take the first element.
    #         plot_refs = self.canvas.axes.plot(xdata, ydata, 'r')
    #         self._plot_ref = plot_refs[0]
    #         # self._plot_ref = plot_refs[1]
    #     else:
    #         # We have a reference, we can use it to update the data for that line.
    #         self._plot_ref.set_ydata(self.ydata)
    #         # self._plot_ref.set_zdata(self.zdata)
    #     # Trigger the canvas to update and redraw.
    #     self.canvas.draw()
    #
    # timer = QtCore.QTimer()
    # timer.setInterval(100)
    # timer.timeout.connect(update_plot(UI))
    # timer.start()

# APP.exec()