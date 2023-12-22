import threading

from PyQt5.QtCore import QThread

from Devices.DAC8563 import DAC8563
from LinearDriver import *
from Devices.AD5664 import *
from Devices.AD8400 import AD8400
from Devices.AD9833 import *
from Controller import *
from Devices.AD7606 import Ad7606
from PyQt5 import QtWidgets, uic


class adcThread(QThread):

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        print('adc')
        time.sleep(0.1)
        ADC_data = controller.get(AD7606_SPI_PORT).read().split()

        while len(ADC_data) == 0:
            continue
        UI.ADC_1.display(int(ADC_data[0]))
        UI.ADC_2.display(int(ADC_data[1]))
        UI.ADC_3.display(int(ADC_data[2]))
        UI.ADC_4.display(int(ADC_data[3]))
        UI.ADC_5.display(int(ADC_data[4]))
        UI.ADC_6.display(int(ADC_data[5]))
        UI.ADC_7.display(int(ADC_data[6]))
        UI.ADC_8.display(int(ADC_data[7]))


if __name__ == '__main__':
    print("Start")

    controller.addDeviceToPort(WaveGen(AD9833_SPI_PORT))
    controller.addDeviceToPort(Ad7606(AD7606_SPI_PORT))

    serialWriterReader.write([23, DAC8563_1_SPI_PORT])
    serialWriterReader.write([27, DAC8563_2_SPI_PORT])

    controller.addDeviceToPort(DAC8563(DAC8563_1_SPI_PORT))
    controller.addDeviceToPort(DAC8563(DAC8563_2_SPI_PORT))

    x_lid = LinearDriver('x')
    y_lid = LinearDriver('y')
    z_lid = LinearDriver('z')

    # controller.get(AD7606_SPI_PORT).read()).decode().split()[0]
    # controller.get(AD9833_SPI_PORT).send_f(1000)
    # controller.get(AD8400_SPI_PORT).setGain(100)

    APP = QtWidgets.QApplication([])
    UI = uic.loadUi("Interface/window_3.ui")


    # ADC_flag = 0

    def updateSLD():
        UI.LCD.display(UI.SLD.value())
        controller.get(AD9833_SPI_PORT).send_freq(UI.SLD.value())


    def updateSLD2():
        UI.LCD2.display(UI.SLD2.value())
        # controller.get(AD9833_SPI_PORT).send_f(UI.SLD2.value())
        controller.get(AD8400_SPI_PORT).setGain(UI.SLD2.value())


    def updateSLD3():
        UI.LCD3.display(UI.SLD3.value())
        # controller.get(AD9833_SPI_PORT).send_f(UI.SLD2.value())
        # controller.get(AD8400_SPI_PORT).setGain(UI.SLD2.value())
        # controller.get(AD5664_SPI_PORT).setChannel(AD56X4_SETMODE_INPUT, AD56X4_CHANNEL_D, UI.SLD3.value())
        # controller.get(AD5664_SPI_PORT).updateChannel(AD56X4_CHANNEL_D)
        # controller.get(AD5664_SPI_PORT).send(UI.SLD3.value(), 0)
        controller.get(DAC8563_2_SPI_PORT).send(UI.SLD3.value(), 0)



    def updateSLD4():
        UI.LCD4.display(UI.SLD4.value())
        # controller.get(AD9833_SPI_PORT).send_f(UI.SLD2.value())
        # controller.get(AD8400_SPI_PORT).setGain(UI.SLD2.value())
        # controller.get(AD5664_SPI_PORT).setChannel(AD56X4_SETMODE_INPUT, AD56X4_CHANNEL_D, UI.SLD3.value())
        # controller.get(AD5664_SPI_PORT).updateChannel(AD56X4_CHANNEL_D)
        # controller.get(AD5664_SPI_PORT).send(UI.SLD4.value(), 1)
        controller.get(DAC8563_2_SPI_PORT).send(UI.SLD4.value(), 1)



    def updateSLD5():
        UI.LCD5.display(UI.SLD5.value())
        # controller.get(AD9833_SPI_PORT).send_f(UI.SLD2.value())
        # controller.get(AD8400_SPI_PORT).setGain(UI.SLD2.value())
        # controller.get(AD5664_SPI_PORT).setChannel(AD56X4_SETMODE_INPUT, AD56X4_CHANNEL_D, UI.SLD3.value())
        # controller.get(AD5664_SPI_PORT).updateChannel(AD56X4_CHANNEL_D)
        # controller.get(AD5664_SPI_PORT).send(UI.SLD5.value(), 2)
        controller.get(DAC8563_1_SPI_PORT).send(UI.SLD5.value(), 0)
        # serialWriterReader.write([22, 2, 8, 0, 1, 0, UI.SLD5.value()])


    def updateSLD6():
        UI.LCD6.display(UI.SLD6.value())
        # controller.get(AD9833_SPI_PORT).send_f(UI.SLD2.value())
        # controller.get(AD8400_SPI_PORT).setGain(UI.SLD2.value())
        # controller.get(AD5664_SPI_PORT).setChannel(AD56X4_SETMODE_INPUT, AD56X4_CHANNEL_D, UI.SLD3.value())
        # controller.get(AD5664_SPI_PORT).updateChannel(AD56X4_CHANNEL_D)
        # controller.get(AD5664_SPI_PORT).send(UI.SLD6.value(), 3)
        controller.get(DAC8563_1_SPI_PORT).send(UI.SLD6.value(), 1)



    def updateSLD7():
        UI.LCD7.display(UI.SLD7.value())


    def pressBX():
        x_lid.activate(500, 750, UI.SLD7.value(), 1)


    def pressFX():
        x_lid.activate(500, 750, UI.SLD7.value(), 0)


    def updateSLD8():
        UI.LCD8.display(UI.SLD8.value())


    def pressBY():
        y_lid.activate(500, 750, UI.SLD8.value(), 1)


    def pressFY():
        y_lid.activate(500, 750, UI.SLD8.value(), 0)


    def updateSLD9():
        UI.LCD9.display(UI.SLD9.value())


    def pressBZ():
        z_lid.activate(500, 500, UI.SLD9.value(), 0)


    def pressFZ():
        z_lid.activate(500, 500, UI.SLD9.value(), 1)


    def tick_timer():
        pass
        # while True:
        #     print('adc')
        #     time.sleep(0.1)
        #     ADC_data = controller.get(AD7606_SPI_PORT).read().split()
        #
        #     while len(ADC_data) == 0:
        #         continue
        #     UI.ADC_1.display(int(ADC_data[0]))
        #     UI.ADC_2.display(int(ADC_data[1]))
        #     UI.ADC_3.display(int(ADC_data[2]))
        #     UI.ADC_4.display(int(ADC_data[3]))
        #     UI.ADC_5.display(int(ADC_data[4]))
        #     UI.ADC_6.display(int(ADC_data[5]))
        #     UI.ADC_7.display(int(ADC_data[6]))
        #     UI.ADC_8.display(int(ADC_data[7]))


    # timer_thread = threading.Thread(target=tick_timer)
    # timer_thread.daemon = True
    # timer_thread.start()

    # updateSLD()
    # updateSLD2()
    # updateSLD3()
    # updateSLD4()
    # updateSLD5()
    # updateSLD6()
    # updateSLD7()
    # updateSLD8()
    # updateSLD9()

    # serialWriterReader.write([23, 3]) # Инициазлизация усилителя
    # serialWriterReader.write([27, 2]) # Инициазлизация усилителя
    UI.SLD.valueChanged.connect(updateSLD)
    UI.SLD2.valueChanged.connect(updateSLD2)
    UI.SLD3.valueChanged.connect(updateSLD3)
    UI.SLD4.valueChanged.connect(updateSLD4)
    UI.SLD5.valueChanged.connect(updateSLD5)
    UI.SLD6.valueChanged.connect(updateSLD6)

    UI.SLD7.valueChanged.connect(updateSLD7)
    UI.BX.clicked.connect(pressBX)
    UI.FX.clicked.connect(pressFX)

    UI.SLD8.valueChanged.connect(updateSLD8)
    UI.BY.clicked.connect(pressBY)
    UI.FY.clicked.connect(pressFY)

    UI.SLD9.valueChanged.connect(updateSLD9)
    UI.BZ.clicked.connect(pressBZ)
    UI.FZ.clicked.connect(pressFZ)

    UI.show()
    APP.exec_()
