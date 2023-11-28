import time
from datetime import datetime

import numpy as np
from matplotlib import pyplot as plt

from Controller import *
from Devices.AD5664 import *
from Devices.AD8400 import *
from Devices.AD7606 import *
from Devices.AD9833 import *
from Devices.DAC8563 import *
from LinearDriver import *

import matplotlib.pyplot as plt
import seaborn as sns

controller.addDeviceToPort(WaveGen(AD9833_SPI_PORT))
controller.addDeviceToPort(Ad7606(AD7606_SPI_PORT))
controller.addDeviceToPort(AD5664(AD5664_SPI_PORT))
controller.addDeviceToPort(AD8400(AD8400_SPI_PORT))

z_lid = LinearDriver('z')

def readADC(ch):
    common_data = controller.get(AD7606_SPI_PORT).read().split()
    while len(common_data) != 8:
        common_data = controller.get(AD7606_SPI_PORT).read().split()
    # print(common_data)
    return (int(common_data[ch-1]))

glrep = 1
direction = 0
freq = 2000
step = 5
rep = 10
plot = 1
gain = 4
channel = 1
delay = 0.4
delayLID = 0.1
oneStep = 25

if __name__ == '__main__':

    serialWriterReader.write([60, 2, gain])

    for n in range(0, glrep, 1):

        current_datetime = datetime.now()
        print("Current date & time : ", current_datetime)
        str_current_datetime = str(current_datetime)
        str_current_datetime = str_current_datetime[:-7]
        str_current_datetime = str_current_datetime.replace(':', '-')
        file_name = str_current_datetime + ' Step_' + str(step) + '.txt'
        afc_name = str_current_datetime + '.png'
        datafile = open("AccLID/X/" + file_name, 'a+')

        z1 = readADC(channel)

        for m in range(0, rep, 1):
            serialWriterReader.write([61, 7, 1])
            z_lid.activate(freq, 500, step, 0)
            time.sleep(delayLID)

            serialWriterReader.write([61, 7, 0])
            time.sleep(delay)
            zmid = readADC(channel)

            serialWriterReader.write([61, 7, 1])
            z_lid.activate(freq, 500, step, 1)

            serialWriterReader.write([61, 7, 0])
            time.sleep(delay)
            z2 = readADC(channel)

            delz = 100*((z2 - z1) * 0.257)/(oneStep*step)
            print(m)
            print(z1, zmid, z2)
            print(delz)
            # if delz<100 and delz>0:
            #     dz.append(delz)
            # print('dz')
            # print(dz)
            z1 = z2
            datafile.write(str(delz) + "\n")
        datafile.close()

    if plot:
        data2 = np.loadtxt("AccLID/X/" + file_name)
        print(data2)

        plt.hist(data2, color='blue', edgecolor='black', bins=int(15))
        plt.title('Histogram of Steps')
        plt.xlabel('Step')
        plt.ylabel('Q')
        plt.savefig("AccLID/X/Picture/" + afc_name, dpi=300)

    plt.show()
    print("finish")
    plt.draw()