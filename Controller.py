class Controller(object):
    def __init__(self):
        self.__spiBus = [0] * 8

    def addDeviceToPort(self, device):
        self.__spiBus[device.getPortNumber()] = device

    def get(self, port):
        return self.__spiBus[port]

    def deleteDeviceFromPort(self, port):
        del self.__spiBus[port]


controller = Controller()

AD9833_SPI_PORT = 1
AD7606_SPI_PORT = 0
DAC8563_1_SPI_PORT = 2
DAC8563_2_SPI_PORT = 3
AD8400_SPI_PORT = 4

# Добаыить + дискреты

