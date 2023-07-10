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

    controller.addDeviceToPort(AD5664(AD5664_SPI_PORT))

    # controller.get(AD7606_SPI_PORT).read()).decode().split()[0]
    controller.get(AD9833_SPI_PORT).send_f(1000)
    controller.get(AD8400_SPI_PORT).setGain(100)

    APP = QtWidgets.QApplication([])
    UI = uic.loadUi("Interface/window_3.ui")

    def updateSLD():
        UI.LCD.display(UI.SLD.value())
        controller.get(AD9833_SPI_PORT).send_f(UI.SLD.value())
        # controller.get(AD9833_SPI_PORT).send_freq(UI.SLD.value())
        #controller.get(AD8400_SPI_PORT).setGain(UI.SLD.value())
    def updateSLD2():
        UI.LCD2.display(UI.SLD2.value())
        #controller.get(AD9833_SPI_PORT).send_f(UI.SLD2.value())
        controller.get(AD8400_SPI_PORT).setGain(UI.SLD2.value())
    def updateSLD3():
        UI.LCD3.display(UI.SLD3.value())
        #controller.get(AD9833_SPI_PORT).send_f(UI.SLD2.value())
        # controller.get(AD8400_SPI_PORT).setGain(UI.SLD2.value())
        # controller.get(AD5664_SPI_PORT).setChannel(AD56X4_SETMODE_INPUT, AD56X4_CHANNEL_D, UI.SLD3.value())
        # controller.get(AD5664_SPI_PORT).updateChannel(AD56X4_CHANNEL_D)
        controller.get(AD5664_SPI_PORT).send(UI.SLD3.value(), 0)
    def updateSLD4():
        UI.LCD4.display(UI.SLD4.value())
        #controller.get(AD9833_SPI_PORT).send_f(UI.SLD2.value())
        # controller.get(AD8400_SPI_PORT).setGain(UI.SLD2.value())
        # controller.get(AD5664_SPI_PORT).setChannel(AD56X4_SETMODE_INPUT, AD56X4_CHANNEL_D, UI.SLD3.value())
        # controller.get(AD5664_SPI_PORT).updateChannel(AD56X4_CHANNEL_D)
        controller.get(AD5664_SPI_PORT).send(UI.SLD4.value(), 1)
    def updateSLD5():
        UI.LCD5.display(UI.SLD5.value())
        #controller.get(AD9833_SPI_PORT).send_f(UI.SLD2.value())
        # controller.get(AD8400_SPI_PORT).setGain(UI.SLD2.value())
        # controller.get(AD5664_SPI_PORT).setChannel(AD56X4_SETMODE_INPUT, AD56X4_CHANNEL_D, UI.SLD3.value())
        # controller.get(AD5664_SPI_PORT).updateChannel(AD56X4_CHANNEL_D)
        controller.get(AD5664_SPI_PORT).send(UI.SLD5.value(), 2)
    def updateSLD6():
        UI.LCD6.display(UI.SLD6.value())
        #controller.get(AD9833_SPI_PORT).send_f(UI.SLD2.value())
        # controller.get(AD8400_SPI_PORT).setGain(UI.SLD2.value())
        # controller.get(AD5664_SPI_PORT).setChannel(AD56X4_SETMODE_INPUT, AD56X4_CHANNEL_D, UI.SLD3.value())
        # controller.get(AD5664_SPI_PORT).updateChannel(AD56X4_CHANNEL_D)
        controller.get(AD5664_SPI_PORT).send(UI.SLD6.value(), 3)


    UI.SLD.valueChanged.connect(updateSLD)
    UI.SLD2.valueChanged.connect(updateSLD2)
    UI.SLD3.valueChanged.connect(updateSLD3)
    UI.SLD4.valueChanged.connect(updateSLD4)
    UI.SLD5.valueChanged.connect(updateSLD5)
    UI.SLD6.valueChanged.connect(updateSLD6)
    UI.show()
    APP.exec()


