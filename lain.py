# ------------------------------------------------------
# ---------------------- lain.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random

import sys
import numpy as np
import random
from PyQt5 import QtCore, QtWidgets, uic

import matplotlib
matplotlib.use('QT5Agg')

import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from AD9833 import *
from Controller import *
from AD7606 import Ad7606
from AD8400 import AD8400
#import matplotlib.pyplot as plt
#import numpy as np
from datetime import datetime

f_start = 7000  #начальная частота
f_stop = 9000   #конечная частота
f_step = 1      #шаг частоты при измерении
gain = 100      #установка усиления

plot = 1        #строить график
repite = 1      #повтор измерений в одной точке
median = 1      #применение медианного фильтра

rep_num = 5     #кол-во повторов в одной точке
adc_channel = 1 #канал АЦП

if __name__ == '__main__':
    serialWriterReader.clean()
    controller.addDeviceToPort(WaveGen(AD9833_SPI_PORT))
    controller.addDeviceToPort(Ad7606(AD7606_SPI_PORT))
    controller.get(AD7606_SPI_PORT).reboot()
    controller.addDeviceToPort(AD8400(AD8400_SPI_PORT))


    class MplWidget(QMainWindow):

        def __init__(self):
            QMainWindow.__init__(self)

            loadUi("Interface/mpl.ui", self)

            self.setWindowTitle("PyQt5 & Matplotlib Example GUI")

            self.pushButton.clicked.connect(self.update_graph)

            #fs = 500
            f = random.randint(1, 10)
            #ts = 1 / fs
            length_of_signal = 1000
            self.t = np.linspace(0, 1, length_of_signal)

            self.cosinus_signal = np.cos(2 * np.pi * f * self.t)
            sinus_signal = np.sin(2 * np.pi * f * self.t)

            self.fig, self.ax1 = plt.subplots()
            self._line1, = self.ax1.plot(self.t, self.cosinus_signal, "r")


            self.plotWidget = FigureCanvas(self.fig)
            lay = QtWidgets.QVBoxLayout(self.widget)
            lay.setContentsMargins(0, 0, 0, 0)
            lay.addWidget(self.plotWidget)
            #self.addToolBar(NavigationToolbar(self.MenuWidget.canvas, self))
            self.addToolBar(QtCore.Qt.TopToolBarArea, NavigationToolbar(self.plotWidget, self))
            #self.addToolBar(MenuWidget, NavigationToolbar(self.plotWidget, self))

        def update_graph(self):
            #fs = 500
            controller.get(AD8400_SPI_PORT).setGain(gain)
            controller.get(AD9833_SPI_PORT).send_f(f_start)
            common_data = controller.get(AD7606_SPI_PORT).read().split()

            a = int(common_data[adc_channel])
            b = a
            c = a

            current_datetime = datetime.now()
            print("Current date & time : ", current_datetime)
            str_current_datetime = str(current_datetime)
            str_current_datetime = str_current_datetime[:-7]
            str_current_datetime = str_current_datetime.replace(':', '-')
            file_name = str_current_datetime + '.txt'
            afc_name = str_current_datetime + '.png'
            datafile = open("Logs/" + file_name, 'a+')

            for m in range(f_start, f_stop, f_step):
                values = []
                controller.get(AD9833_SPI_PORT).send_f(m)
                # datafile = open("Logs/" + file_name, 'a+')
                time.sleep(0.0001)

                if repite:
                    point_sum = 0
                    for i in range(0, rep_num, 1):
                        common_data = controller.get(AD7606_SPI_PORT).read().split()
                        if len(common_data) == 0:
                            continue
                        point_sum = point_sum + int(common_data[adc_channel])
                    amplitude = point_sum / rep_num
                else:
                    common_data = controller.get(AD7606_SPI_PORT).read().split()
                    if len(common_data) == 0:
                        continue
                    amplitude = int(common_data[adc_channel])

                # if median:
                #     c = b
                #     b = a
                #     a = amplitude
                #     amplitude_data = max(a, c) if (max(a, b) == max(b, c)) else max(b, min(a, c))
                # else:
                #     amplitude_data = amplitude

                c = b
                b = a
                a = amplitude
                amplitude_meddle = max(a, c) if (max(a, b) == max(b, c)) else max(b, min(a, c))

                datafile.write(str(m) + ' ' + str(amplitude) + ' ' + str(amplitude_meddle) + "\n")
            datafile.close()

            if plot:
                datafile = open("Logs/" + file_name, 'a+')
                datafile.write(
                    "START " + str(f_start) + "\n" + "STOP " + str(f_stop) + "\n" + "STEP " + str(f_step) + "\n")
                data2 = np.loadtxt("Logs/" + file_name)
                x = data2[:, 0]
                y = data2[:, 1]
                z = data2[:, 2]
                # plt.plot(x, y, 'r:')
                # plt.plot(x, z, 'g--')
                # plt.title('Резонанс датчика')
                # plt.xlabel('Частота, КГц')
                # plt.ylabel('Амплитуда')
                # plt.grid(1, 'both', 'both')
                # plt.axis([f_start, f_stop, 0, round(max(y), -4) + 5000])
                # plt.savefig("Logs/" + afc_name, dpi=300)
            datafile.close()
            # f = random.randint(1, 10)
            # # ts = 1 / fs
            # # length_of_signal = 1000
            # # t = np.linspace(0, 1, length_of_signal)
            #
            # self.cosinus_signal = np.cos(2 * np.pi * f * self.t)
            # #sinus_signal = np.sin(2 * np.pi * f * t)
             #self._line1.set_data(self.t, self.cosinus_signal)


            self._line1.set_data(x, y)
            self._line1.figure.canvas.draw()
            # self.MplWidget.canvas.axes.clear()
            # self.MplWidget.canvas.axes.plot(t, cosinus_signal)
            # self.MplWidget.canvas.axes.plot(t, sinus_signal)
            # self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
            # self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
            # self.MplWidget.canvas.draw()


    app = QtWidgets.QApplication(sys.argv)
    window = MplWidget()
    window.show()
    app.exec_()