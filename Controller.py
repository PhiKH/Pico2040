class Controller(object):
    def __init__(self):
        self.__spiBus = [0] * 8

    def addDeviceToPort(self, device, port):
        self.__spiBus[port] = device

    def get(self, port):
        self.__spiBus[port].setPort(port)
        return self.__spiBus[port]

    def deleteDeviceFromPort(self, port):
        del self.__spiBus[port]


controller = Controller()

WAVE_GEN_SPI_PORT = 1
