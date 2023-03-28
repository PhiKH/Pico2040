import time
from AD9833 import *
from Controller import *
from AD7606 import Ad7606
from AD8400 import AD8400

if __name__ == '__main__':

    # controller.addDeviceToPort(WaveGen(AD9833_SPI_PORT), AD9833_SPI_PORT) # todo fix double define
    # controller.addDeviceToPort(Ad7606(AD7606_SPI_PORT), AD7606_SPI_PORT)
    controller.addDeviceToPort(AD8400(AD8400_SPI_PORT), AD8400_SPI_PORT)

    x = 15000
    gain = 20
    while True:

        controller.get(AD8400_SPI_PORT).setGain(0)
        # controller.get(AD8400_SPI_PORT).setGain(255)

        # controller.get(AD9833_SPI_PORT).send_f(x)
        # print(controller.get(AD7606_SPI_PORT).read())
        # controller.get(AD7606_SPI_PORT).reboot()
        # print(serialWriterReader.read(100))

        # time.sleep(0.2)
        x += 100
        # time.sleep(0.1)
        # print(serialWriterReader.read(400))
        # serialWriterReader.write(['abcde'])
        # time.sleep(1)
        if x > 20000:
            x = 15000
