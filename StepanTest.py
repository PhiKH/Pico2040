import random
import threading
import time
from AD5664 import *
from AD8400 import AD8400
from AD9833 import *
from Controller import *
from AD7606 import Ad7606
from PyQt5 import QtWidgets, uic

if __name__ == '__main__':
    print("Start")

    controller.addDeviceToPort(WaveGen(AD9833_SPI_PORT))
    controller.addDeviceToPort(Ad7606(AD7606_SPI_PORT))
    controller.addDeviceToPort(AD8400(AD8400_SPI_PORT))

    # controller.addDeviceToPort(AD5664(AD5664_SPI_PORT))

    # controller.get(AD7606_SPI_PORT).read()).decode().split()[0]
    controller.get(AD9833_SPI_PORT).send_f(20000)

    APP = QtWidgets.QApplication([])
    UI = uic.loadUi("Interface/window_2.ui")

    def updateSLD():
        UI.LCD.display(UI.SLD.value())
        controller.get(AD9833_SPI_PORT).send_f(UI.SLD.value())
        # controller.get(AD8400_SPI_PORT).setGain(UI.SLD.value())

    UI.SLD.valueChanged.connect(updateSLD)
    UI.show()
    APP.exec()

