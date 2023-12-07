from SerialManager import serialWriterReader


class Ad7606:
    def __init__(self, port):
        self.__numPort = port
        self.__bitPerWord = 16
        self.__chpa = 0
        self.__cpol = 1
        self.__serial = serialWriterReader

    def __getSettings(self):
        return [self.__numPort, self.__bitPerWord, self.__chpa, self.__cpol]

    def reboot(self):
        self._send(11, [0])

    def enable(self):
        self._send(6, [0])

    def disable(self):
        self._send(6, [1])

    def read(self):
        # self.reboot()
        self._send(12, [0])
        return self.__serial.read(1000).decode()
    def getValueFromChannel(self, channel):
        self.__serial.write([24, channel - 1])
        return self.__serial.read(100).decode()
    def activateScanning(self, n, start_freq, step, channel = 1, delay = 10):
        self.__serial.write([25, n, start_freq, step, channel, delay])

    def stopScanning(self):
        self.__serial.write([26])

    def getPortNumber(self):
        return self.__numPort

    def _send(self, code, value):
        return self.__serial.write([code] + self.__getSettings() + value)
