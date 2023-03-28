class Controller(object):
    def __init__(self):
        self.__spiBus = [0] * 8

    def addDeviceToPort(self, device, port):
        self.__spiBus[port] = device

    def get(self, port):
        return self.__spiBus[port]

    def deleteDeviceFromPort(self, port):
        del self.__spiBus[port]


controller = Controller()

AD9833_SPI_PORT = 2
AD7606_SPI_PORT = 0
AD8400_SPI_PORT = 1
