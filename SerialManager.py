from serial import Serial


class SerialWriter(object):

    def __init__(self):
        self.__serial = Serial('COM5', 115200, timeout=0.1)

    def write(self, value):
        txs = ' '.join(map(str, value)).encode()
        self.__serial.write(txs)

    def read(self, size):
        return self.__serial.readline(size)


serialWriterReader = SerialWriter()
