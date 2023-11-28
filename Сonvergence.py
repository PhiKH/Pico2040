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

direction = 1
freq = 3000
step = 5
gain = 4
channel = 1
Zmax = 31000
Zmin = 10000
delay = 0.4

if __name__ == '__main__':
    print('Start')
    serialWriterReader.write([60, 2, gain])

    flag = 1

    while flag:
        serialWriterReader.write([61, 7, 1])
        z_lid.activate(freq, 500, step, direction)
        serialWriterReader.write([61, 7, 0])
        time.sleep(delay)
        z = readADC(channel)
        print(z)
        if z<Zmax:
            flag = 0
    print('Stop, Z =')
    print(z)
