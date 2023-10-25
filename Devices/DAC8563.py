from Devices.BasicDevice import BasicDevice
from SerialManager import serialWriterReader

class DAC8563(BasicDevice):
    def __init__(self, port):
        super().__init__()
        self.__numPort = port
        self.__bitPerWord = 8
        self.__chpa = 1
        self.__cpol = 0
        self.__serial = serialWriterReader

    def __getSettings(self):
        return [self.__numPort, self.__bitPerWord, self.__chpa, self.__cpol]

    def getPortNumber(self):
        return self.__numPort

    def send(self, value, channel):
        self.__serial.write([22] + self.__getSettings() + [value, channel])
