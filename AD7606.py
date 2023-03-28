from SerialManager import serialWriterReader


#   todo decoder
#   todo conv busy     IN_BUSY OUT_CONV IN_CONV

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

    def read(self):
        # self.reboot()
        self._send(12, [0])
        return self.__serial.read(100)

    def _send(self, code, value):
        return self.__serial.write([code] + self.__getSettings() + value)
