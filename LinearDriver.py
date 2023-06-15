from SerialManager import serialWriterReader

class LinearDriver:
    def __init__(self, z):
        self.__serial = serialWriterReader
        self.__code = 100
        if z == 'y':
            self.__code = 105
        if z == 'z':
            self.__code = 110

    def activate(self, f, p, n, d):
        self._send(self.__code, [f, p, n, d])

    def _send(self, code, value):
        return self.__serial.write([code] + value)
