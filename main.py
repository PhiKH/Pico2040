import time
from AD9833 import *
from Controller import *


if __name__ == '__main__':
    # controller.addDeviceToPort(WaveGen(WAVE_GEN_SPI_PORT), WAVE_GEN_SPI_PORT)
    # controller.get(WAVE_GEN_SPI_PORT).send_f(5000)
    # a = serialWriterReader.read(300)
    # print(a)

    while True:
        print(serialWriterReader.read(100))
        time.sleep(1)
