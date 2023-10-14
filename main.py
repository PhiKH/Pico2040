import random
import threading
import time

from LinearDriver import *
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
STEP = 10
REP = 1

if __name__ == '__main__':

    serialWriterReader.write([23, 3])
    time.sleep(0.01)
    a = 1000
    while True:
        # print(serialWriterReader.read(1000).decode())
        serialWriterReader.write([22, 3, 8, 0, 1, 0, a])
        serialWriterReader.write([22, 3, 8, 0, 1, 1, a])
        a = a + 100
        time.sleep(0.01)

    #
    # serialWriterReader.write([7])  # Начать скан в текущей точке
    # exit(0)


    # serialWriterReader.write([52]) # Остановить скан
    # exit(0)
    #
    # serialWriterReader.clean()
    # serialWriterReader.write([55, 100, 100, 0, 0, 10, 1, 500, 5000, 0])  # Обновить конфиг
    # time.sleep(0.01)
    # serialWriterReader.write([50, 100, 100])  # начать скан в точке 100 100
    # exit(0)


    # serialWriterReader.write([51, 50000, 50000, 50]) # Перемещение в 100;100 с задержкой 10

    # while True:
    #     serialWriterReader.write([51, 65000, 65000, 0])  # Перемещение в 100;100 с задержкой 10
    #     t = ''
    #     while 'END' not in t:
    #         t = serialWriterReader.read(100).decode()
    #     serialWriterReader.write([51, 0, 0, 0])  # Перемещение в 100;100 с задержкой 10
    #     t = ''
    #     while 'END' not in t:
    #         t = serialWriterReader.read(100).decode()



    # x_lid = LinearDriver('x')
    # y_lid = LinearDriver('y')
    # z_lid = LinearDriver('z')
    # x_lid.activate(50, 500, 100, 1) # TODO Управление лидом freq, p, n_steps, direction
    # z_lid.activate(50, 500, 100, 1) # TODO Управление лидом freq, p, n_steps, direction
    # y_lid.activate(50, 500, 100, 1) # TODO Управление лидом freq, p, n_steps, direction
    # serialWriterReader.write([70])
    # time.sleep(0.5)
    # serialWriterReader.write([80, 99 ,5000, 750, 100, 1])
    # while True
    #     print(serialWriterReader.read(10000))

    # exit(0)


    controller.addDeviceToPort(WaveGen(AD9833_SPI_PORT))
    controller.addDeviceToPort(Ad7606(AD7606_SPI_PORT))
    # controller.get(AD7606_SPI_PORT).reboot()

    # controller.get(AD9833_SPI_PORT).send_f(15000)
    controller.addDeviceToPort(AD5664(AD5664_SPI_PORT))
    controller.addDeviceToPort(AD8400(AD8400_SPI_PORT))
    controller.get(AD8400_SPI_PORT).setGain(200)  # TODO Установить усиление [0.255]

    # controller.get(AD7606_SPI_PORT).enable()
    # controller.get(AD7606_SPI_PORT).disable()

    # controller.get(AD7606_SPI_PORT).activateScanning(400, 7000, 5, 1, 0) # TODO Запустить снятие ачх'
    # time.sleep(2)
    # controller.get(AD7606_SPI_PORT).stopScanning()

    # t = ''
    # while t == '':
    #     t = serialWriterReader.read(100000).decode()
    #
    # print(t)
    # t = t.split(sep=',')


    # controller.get(AD9833_SPI_PORT).send_f(7600)
    # exit(0)
    # controller.get(AD8400_SPI_PORT).setGain(200)  # TODO Установить усиление [0..255]

    x = 5000
    gain = 40

    # controller.get(AD8400_SPI_PORT).setGain(100)
    # for n in range(0, 100, STEP):
    #     controller.get(AD7606_SPI_PORT).activateScanning(400, 7000, 5, 1, 10)
    #     t = ''
    #     while t == '':
    #         t = serialWriterReader.read(100000).decode()
    #
    #     print(t)
    #     t = t.split(sep=',')
    serialWriterReader.write([60, 2, 3]) # TODO установить значение на порт port[1...3],value[0...3](IO1/3)/[0...7](IO2)
    # serialWriterReader.write([61, 4, 0])  # TODO установить значение на пин pin[1...7],value[0...1]
    # exit(0)
    while 0:
        controller.get(AD9833_SPI_PORT).send_f(15000)
        # time.sleep(0.1)
        # print(serialWriterReader.read(10000000).decode())
        # controller.get(AD8400_SPI_PORT).setGain(100)
        # controller.get(AD7606_SPI_PORT).activateScanning(400, 7000, 5, 1, 10)
        # x_lid.activate(500, 750, 1000, 0)  # TODO Управление лидом freq, p, n_steps, direction
        # time.sleep(1)
        # controller.get(AD5664_SPI_PORT).send(32000, 1)


    while 1:

        # controller.get(AD5664_SPI_PORT).setChannel(AD56X4_SETMODE_INPUT, AD56X4_CHANNEL_D, x)
        # controller.get(AD5664_SPI_PORT).send(10000 + x, 1) # TODO установить значение на ЦАП [value, channel]
        # controller.get(AD8400_SPI_PORT).setGain(10)
        # print(controller.get(AD7606_SPI_PORT).getValueFromChannel(1), end=' ')
        # print(serialWriterReader.read(10000000).decode())
        controller.get(AD9833_SPI_PORT).send_f(15000)

        print(controller.get(AD7606_SPI_PORT).read(), end=' ')   # TODO Прочитать с ацп
        time.sleep(0.001)
        # controller.get(AD9833_SPI_PORT).send_freq(x) # TODO Установить частоту на генератор
        # controller.get(AD8400_SPI_PORT).setGainWithoutSets(gain)  # TODO Установить усиление [0..255]

        # t = serialWriterReader.read(100000)
        # print(t)
        # time.sleep(0.001)
        x += 100
        # print(x)
        # gain += 5
        # if gain >= 255:
        #     gain = 40
        # if x > 30000:
        #     x = 4000

    for n in range(1, 256, 1):

        current_datetime = datetime.now()
        print("Current date & time : ", current_datetime)
        str_current_datetime = str(current_datetime)
        str_current_datetime = str_current_datetime[:-7]
        str_current_datetime = str_current_datetime.replace(':', '-')
        # print(str_current_datetime)
        file_name = str_current_datetime + '.txt'
        afc_name = str_current_datetime + '.png'

        # controller.get(AD8400_SPI_PORT).setGain(50 + 40 * n)  # TODO Установить усиление [0..255]
        controller.get(AD8400_SPI_PORT).setGain(n)
        for m in range(BEGIN, END, STEP):
            values = []
            controller.get(AD9833_SPI_PORT).send_f(m)
            datafile = open("Logs/" + file_name, 'a+')
            time.sleep(0.005)
            li = controller.get(AD7606_SPI_PORT).read().split()
            if len(li) == 0:
                continue
            datafile.write(str(m) + ' ' + str(li[1]) + "\n")
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
