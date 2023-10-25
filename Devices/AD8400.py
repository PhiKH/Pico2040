from SerialManager import serialWriterReader

class AD8400:
    def __init__(self, port):
        self.__numPort = port
        self.__bitPerWord = 8
        self.__chpa = 0
        self.__cpol = 0
        self.__serial = serialWriterReader
        self.__gain = 128

    def setGain(self, gain):
        if gain < 0:
            gain = 0
        if gain > 255:
            gain = 255

        self.__gain = gain
        self._send(5, [gain])

    def getGain(self):
        return self.__gain

    def setGainWithoutSets(self, gain):
        self.__serial.write([40, gain])

    def __getSettings(self):
        return [self.__numPort, self.__bitPerWord, self.__chpa, self.__cpol]

    def _send(self, code, value):
        return self.__serial.write([code] + self.__getSettings() + value)

    def getPortNumber(self):
        return self.__numPort
