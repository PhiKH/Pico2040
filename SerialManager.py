from serial import Serial

class SerialWriter(object):

    def __init__(self):
        self.__serial = Serial('COM9', 400000000, timeout=0.00005)

    def write(self, value):
        txs = (','.join(map(str, value)) + '\n').encode()
        print('Write to Serial', txs)
        self.__serial.write(txs)

    def read(self, size):
        return self.__serial.readline(size)

    def clean(self):
        while self.isAvailable():
            self.__serial.readline()

    def isAvailable(self):
        return self.__serial.in_waiting


serialWriterReader = SerialWriter()
