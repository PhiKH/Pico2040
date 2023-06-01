import random
import threading
import time

from AD5664 import *
from AD9833 import *
from Controller import *
from AD7606 import Ad7606
from AD8400 import AD8400
from threading import Thread
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Блокирующее чтение
# ЦАп для 4 каналов
# поток для ацп
# фикс время
# защита от неправильного выключения

BEGIN = 7000
END = 9000
STEP = 5
REP = 10

if __name__ == '__main__':

    controller.addDeviceToPort(WaveGen(AD9833_SPI_PORT))
    controller.addDeviceToPort(Ad7606(AD7606_SPI_PORT))
    # controller.get(AD9833_SPI_PORT).send_f(15000)
    # controller.addDeviceToPort(AD5664(AD5664_SPI_PORT))
    # controller.addDeviceToPort(AD8400(AD8400_SPI_PORT))

    # controller.get(AD7606_SPI_PORT).enable()
    # controller.get(AD7606_SPI_PORT).disable()


    x = 5000
    gain = 1
    while True:

        # controller.get(AD5664_SPI_PORT).setChannel(AD56X4_SETMODE_INPUT, AD56X4_CHANNEL_D, x)
        # controller.get(AD5664_SPI_PORT).updateChannel(AD56X4_CHANNEL_D)
        # controller.get(AD8400_SPI_PORT).setGain(10)
        print(controller.get(AD7606_SPI_PORT).read())
        controller.get(AD9833_SPI_PORT).send_f(x)
        # print(serialWriterReader.read(100))
        # controller.get(AD7606_SPI_PORT).reboot()
        # time.sleep(0.00001)
        x += 100
        # print(x)
        gain += 1
        if gain >= 255:
            gain = 5
        if x > 30000:
            x = 4000

    current_datetime = datetime.now()
    print("Current date & time : ", current_datetime)
    str_current_datetime = str(current_datetime)
    str_current_datetime = str_current_datetime[:-7]
    str_current_datetime = str_current_datetime.replace(':', '-')
    # print(str_current_datetime)
    file_name = str_current_datetime + '.txt'
    afc_name = str_current_datetime + '.png'
    # print(file_name)

    for n in range(BEGIN, END, STEP):
        values = []
        time.sleep(0.0)
        for m in range(0, REP):
            controller.get(AD9833_SPI_PORT).send_f(n)
        # print(controller.get(AD7606_SPI_PORT).read().decode().split())
            values.insert(m, (controller.get(AD7606_SPI_PORT).read()).decode().split()[1])
        values.sort()
        datafile = open("Logs/" + file_name, 'a+')
        datafile.write(str(n) + ' ' + str(values[int(REP / 2)]) + "\n")
        datafile.close()

    datafile = open("Logs/" + file_name, 'a+')
    datafile.write("REP" + str(REP) + "\n" + "STEP" + str(STEP) + "\n")
    data2 = np.loadtxt("Logs/" + file_name)
    x = data2[:, 0]
    y = data2[:, 1]
    plt.plot(x, y, 'r--')
    plt.title('Резонанс датчика')
    plt.xlabel('Частота, КГц')
    plt.ylabel('Амплитуда')
    plt.grid(1)
    plt.savefig("Logs/" + afc_name, dpi=100)
    plt.show()
    print("finish")
    plt.draw()
