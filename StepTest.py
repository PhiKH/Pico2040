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


if __name__ == '__main__':
    # plt.hist([1.53, 4.59, -6.12, -0.36, 2.9699999999999998, -4.859999999999999, -0.36, 11.25, -9.629999999999999, 4.859999999999999, -2.25, 7.199999999999999, -5.67, -0.09, 2.61, -5.3999999999999995, -3.2399999999999998, -2.16, 9.54, -1.6199999999999999, 1.7999999999999998, -8.1, 32.04, -22.32, 3.42, -11.16, 3.51, 3.2399999999999998, -1.44, 1.71, -3.96, -5.04, 4.59, -2.6999999999999997, 1.26, 1.71, -6.029999999999999, 14.309999999999999, -5.85, 0.0, 5.49, 0.09, -9.45, -3.8699999999999997, 0.18, 3.33, 0.27, -2.9699999999999998], color='blue', edgecolor='black',
    #          bins=int(20))
    # plt.show()
    # exit(0)

    serialWriterReader.write([60, 2, 4])
    dz = []

    # common_data = controller.get(AD7606_SPI_PORT).read().split()
    # while len(common_data) != 8:
    #     common_data = controller.get(AD7606_SPI_PORT).read().split()
    # z1 = int(common_data[1])
    # while z1 > 30000:
    common_data = controller.get(AD7606_SPI_PORT).read().split()
    while len(common_data) != 8:
        common_data = controller.get(AD7606_SPI_PORT).read().split()
    print(common_data)
    z1 = int(common_data[0])

    for m in range(0, 100, 1):
        # z_lid.activate(2000, 500, 20, 1)
        if z1<30000 and z1>3000:
            # time.sleep(0.1)
            # if z1 < 10000:
            #     break

            serialWriterReader.write([61, 7, 1])
            z_lid.activate(2000, 500, 20, 1)
            serialWriterReader.write([61, 7, 0])
            time.sleep(0.4)

            # rep_num = 5
            # point_sum = 0
            # for i in range(0, rep_num, 1):
            #     common_data = controller.get(AD7606_SPI_PORT).read().split()
            #     while len(common_data) == 0:
            #         common_data = controller.get(AD7606_SPI_PORT).read().split()
            #
            #     time.sleep(0.001)
            #     if len(common_data) != 8:
            #         continue
            #     point_sum = point_sum + int(common_data[1])
            # z2 = point_sum / rep_num

            # common_data = controller.get(AD7606_SPI_PORT).read().split()
            # while len(common_data) != 8:
            #     common_data = controller.get(AD7606_SPI_PORT).read().split()
            # z2 = int(common_data[1])
            # time.sleep(0.1)
            # while z2 > 30000:
            common_data = controller.get(AD7606_SPI_PORT).read().split()
            while len(common_data) != 8:
                common_data = controller.get(AD7606_SPI_PORT).read().split()
            print(common_data)
            z2 = int(common_data[0])

            delz = (z2-z1)*0.09
            print(delz)
            if delz<100 and delz>0:
                dz.append(delz)
            print(z1, z2)
            print('dz')
            print(dz)
            z1 = z2


    # matplotlib histogram
    plt.hist(dz, color='blue', edgecolor='black',
             bins=int(10))

    # Add labels
    # plt.title('Histogram of Arrival Delays')
    # plt.xlabel('Delay (min)')
    # plt.ylabel('Flights')
    plt.show()