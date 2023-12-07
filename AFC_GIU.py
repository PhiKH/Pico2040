import sys
import random
from PyQt5 import QtWidgets, uic

import matplotlib
matplotlib.use('QT5Agg')

import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
import numpy as np
from datetime import datetime
from Devices.AD9833 import *
from Controller import *
from Devices.AD7606 import Ad7606
from Devices.AD8400 import AD8400
f_start = 7000  #начальная частота
f_stop = 9000   #конечная частота
f_step = 10      #шаг частоты при измерении
gain = 250      #установка усиления

plot = 1        #строить график
repite = 1      #повтор измерений в одной точке
median = 0      #применение медианного фильтра
logfile = 0     #запись в файл
rep_num = 5     #кол-во повторов в одной точке
adc_channel = 1 #канал АЦП

flag1 = 0
limX = 50
period = 10
n_data = limX
xdata = list(range(n_data))
adata = [random.randint(0, 10) for i in range(n_data)]
# class MyWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         uic.loadUi('test.ui', self)
#         # self.flag_1 = 0
#         self.fig, self.ax1 = plt.subplots()
#
#         self.n_data = limX
#         self.xdata = list(range(self.n_data))
#         self.adata = [random.randint(0, 10) for i in range(self.n_data)]
#         self._line1, = self.ax1.plot(self.xdata, self.adata, "r")
#
#         self.bdata = [random.randint(10, 20) for i in range(self.n_data)]
#         self._line2, = self.ax1.plot(self.xdata, self.bdata, "g")
#
#         self.cdata = [random.randint(20, 30) for i in range(self.n_data)]
#         self._line3, = self.ax1.plot(self.xdata, self.cdata, "b")
#
#         self.ddata = [random.randint(30, 40) for i in range(self.n_data)]
#         self._line4, = self.ax1.plot(self.xdata, self.ddata, "y")
#
#         # self.ax1.title('OSC')
#         # self.ax1.xlabel('Частота, КГц')
#         # self.ax1.ylabel('Амплитуда')
#         self.ax1.grid(1, 'both', 'both')
#         self.plotWidget = FigureCanvas(self.fig)
#         lay = QtWidgets.QVBoxLayout(self.content_plot)
#         lay.setContentsMargins(0, 0, 0, 0)
#         lay.addWidget(self.plotWidget)
#         # add toolbar
#         self.addToolBar(QtCore.Qt.TopToolBarArea, NavigationToolbar(self.plotWidget, self))
#
#         self._timer = self.plotWidget.new_timer(period)
#         self._timer.add_callback(self._update_canvas)
#         self._timer.start()
#
#     def _update_canvas(self):
#         if flag1:
#             self.adata = self.adata[1:] + [random.randint(0, 10)]
#             self._line1.set_data(self.xdata, self.adata)
#             self._line1.figure.canvas.draw()
#
#             self.bdata = self.bdata[1:] + [random.randint(10, 20)]
#             self._line2.set_data(self.xdata, self.bdata)
#             self._line2.figure.canvas.draw()
#
#             self.cdata = self.cdata[1:] + [random.randint(20, 30)]
#             self._line3.set_data(self.xdata, self.cdata)
#             self._line3.figure.canvas.draw()
#
#             self.ddata = self.ddata[1:] + [random.randint(30, 40)]
#             self._line4.set_data(self.xdata, self.ddata)
#             self._line4.figure.canvas.draw()
#             # print('UP')

if __name__ == '__main__':
    serialWriterReader.clean()
    controller.addDeviceToPort(WaveGen(AD9833_SPI_PORT))
    controller.addDeviceToPort(Ad7606(AD7606_SPI_PORT))
    controller.get(AD7606_SPI_PORT).reboot()
    controller.addDeviceToPort(AD8400(DAC8563_1_SPI_PORT))
    controller.get(DAC8563_1_SPI_PORT).setGain(gain)
    controller.get(AD9833_SPI_PORT).send_f(f_start)
    common_data = controller.get(AD7606_SPI_PORT).read().split()
    # time.sleep(0.01)
    while len(common_data) == 0:
        continue
    a = int(common_data[adc_channel])
    b = a
    c = a
    app = QtWidgets.QApplication(sys.argv)
    # window = MyWindow()
    # APP = QtWidgets.QApplication([])
    UI = uic.loadUi("Interface/window_5.ui")
    # super(MyWindow, self).__init__()
    # UI = uic.loadUi('test.ui', self)
    # self.flag_1 = 0
    fig, ax1 = plt.subplots()
    _line1, = ax1.plot(0, 0, "r")
    # n_data = limX
    # xdata = list(range(n_data))
    # adata = [random.randint(0, 10) for i in range(n_data)]
    # _line1, = ax1.plot(xdata, adata, "r")

    # self.bdata = [random.randint(10, 20) for i in range(self.n_data)]
    # self._line2, = self.ax1.plot(self.xdata, self.bdata, "g")
    #
    # self.cdata = [random.randint(20, 30) for i in range(self.n_data)]
    # self._line3, = self.ax1.plot(self.xdata, self.cdata, "b")
    #
    # self.ddata = [random.randint(30, 40) for i in range(self.n_data)]
    # self._line4, = self.ax1.plot(self.xdata, self.ddata, "y")

    # self.ax1.title('OSC')
    # self.ax1.xlabel('Частота, КГц')
    # self.ax1.ylabel('Амплитуда')
    ax1.grid(1, 'both', 'both')
    plotWidget = FigureCanvas(fig)
    lay = QtWidgets.QVBoxLayout(UI.content_plot)
    lay.setContentsMargins(0, 0, 0, 0)
    lay.addWidget(plotWidget)
    # add toolbar
    # UI.addToolBar(QtCore.Qt.TopToolBarArea, NavigationToolbar(plotWidget))

    # self._timer = self.plotWidget.new_timer(period)
    # self._timer.add_callback(self._update_canvas)
    # self._timer.start()

    def start_stop():
        # n_data = limX
        # xdata = list(range(n_data))
        # adata = [random.randint(0, 10) for i in range(n_data)]
        # global adata
        # adata = adata[1:] + [random.randint(0, 10)]
        # _line1.set_data(xdata, adata)
        # _line1.figure.canvas.draw()
        # global flag1
        # if flag1:
        #     flag1 = 0
        # else:
        #     flag1 = 1
        buffer = []
        if logfile:
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
                # print(int(100*(m-f_start)/(f_stop-f_start)))
                UI.progressBar.setValue(int(100 * (m - f_start) / (f_stop - f_start)) + 1)
                controller.get(AD9833_SPI_PORT).send_f(m)
                # datafile = open("Logs/" + file_name, 'a+')
                time.sleep(0.0001)

                if repite:
                    point_sum = 0
                    for i in range(1, rep_num + 1, 1):
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

                print('median start')

                if median:
                    print('median start 2')
                    global c
                    global b
                    global a
                    c = b
                    b = a
                    a = amplitude
                    amplitude = max(a, c) if (max(a, b) == max(b, c)) else max(b, min(a, c))

                else:
                    print('median start 3')
                    amplitude = amplitude

                # c = b
                # b = a
                # a = amplitude
                # amplitude_meddle = max(a, c) if (max(a, b) == max(b, c)) else max(b, min(a, c))

                datafile.write(str(m) + ' ' + str(amplitude) + "\n")
            datafile.close()
            # exit(0)
            if plot:
                datafile = open("Logs/" + file_name, 'a+')
                datafile.write(
                    "START " + str(f_start) + "\n" + "STOP " + str(f_stop) + "\n" + "STEP " + str(f_step) + "\n")
                data2 = np.loadtxt("Logs/" + file_name)
                x = data2[:, 0]
                y = data2[:, 1]
                # z = data2[:, 2]
                # ax1.plot(x, y, "r")
                ax1.axis([f_start, f_stop, 0, round(max(y), -4) + 5000])
                _line1.set_data(x, y)
                _line1.figure.canvas.draw()
                print('stop')
                # plt.plot(x, y, 'r:')
                # plt.plot(x, z, 'g--')
                # plt.title('Резонанс датчика')
                # plt.xlabel('Частота, КГц')
                # plt.ylabel('Амплитуда')
                # plt.grid(1, 'both', 'both')
                # plt.savefig("Logs/" + afc_name, dpi=300)
            datafile.close()
        else:
            print('строим из буфера')
            for m in range(f_start, f_stop, f_step):
                values = []
                # print(int(100*(m-f_start)/(f_stop-f_start)))
                UI.progressBar.setValue(int(100 * (m - f_start) / (f_stop - f_start)) + 1)
                controller.get(AD9833_SPI_PORT).send_f(m)
                # datafile = open("Logs/" + file_name, 'a+')
                time.sleep(0.0001)

                if repite:
                    point_sum = 0
                    for i in range(1, rep_num + 1, 1):
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

                if median:
                    # global c
                    # global b
                    # global a
                    c = b
                    b = a
                    a = amplitude
                    amplitude = max(a, c) if (max(a, b) == max(b, c)) else max(b, min(a, c))

                else:
                    amplitude = amplitude

                buffer.append([m, amplitude])
                # z = data2[:, 2]
                # ax1.plot(x, y, "r")

            m_values = [int(pair[0]) for pair in buffer]
            amplitude_values = [float(pair[1]) for pair in buffer]
            ax1.axis([f_start, f_stop, 0, round(max(amplitude_values), -4) + 5000])
            _line1.set_data(m_values, amplitude_values)
            _line1.figure.canvas.draw()
            print('stop')



    # def updateSLD1():
    #     UI.LCD1.display(UI.SLD1.value())
    #     global f_start
    #     f_start = UI.SLD1.value()
    #
    # def updateSLD2():
    #     UI.LCD2.display(UI.SLD2.value())
    #     global f_stop
    #     f_stop = UI.SLD2.value()
    #
    # def updateSLD3():
    #     UI.LCD3.display(UI.SLD3.value())
    #     global f_step
    #     f_step = UI.SLD3.value()

    def updateL_1():
        global f_start
        f_start = int(UI.L_1.text())
    def updateL_2():
        global f_stop
        f_stop = int(UI.L_2.text())
    def updateL_3():
        global f_step
        f_step = int(UI.L_3.text())
    def updateL_4():
        global rep_num
        rep_num = int(UI.L_4.text())
    def updateChB_1():
        global median
        median = UI.ChB_1.checkState()
        print(median)

    def updateChB_2():
        global logfile
        logfile = UI.ChB_2.checkState()
        print(logfile)

    # UI.LCD1.display(UI.SLD1.value())
    # UI.LCD2.display(UI.SLD2.value())
    # UI.LCD3.display(UI.SLD3.value())
    UI.L_1.setText(str(f_start))
    UI.L_2.setText(str(f_stop))
    UI.L_3.setText(str(f_step))
    UI.L_4.setText(str(rep_num))
    UI.BTN1.clicked.connect(start_stop)

    UI.L_1.editingFinished.connect(updateL_1)
    UI.L_2.editingFinished.connect(updateL_2)
    UI.L_3.editingFinished.connect(updateL_3)
    UI.L_4.editingFinished.connect(updateL_4)
    UI.ChB_1.stateChanged.connect(updateChB_1)
    UI.ChB_2.stateChanged.connect(updateChB_2)
    # UI.SLD1.valueChanged.connect(updateSLD1)
    # UI.SLD2.valueChanged.connect(updateSLD2)
    # UI.SLD3.valueChanged.connect(updateSLD3)
    UI.show()
    sys.exit(app.exec_())
