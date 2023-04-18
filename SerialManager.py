from serial import Serial
from threading import Lock

mutex = Lock()

class SerialWriter(object):

    def __init__(self):
        self.__serial = Serial('COM8', 115200, timeout=0.1)

    def write(self, value):
        mutex.acquire()
        txs = (','.join(map(str, value)) + '\n').encode()
        # print('Write to Serial', txs)
        self.__serial.write(txs)
        mutex.release()

    def read(self, size):
        return self.__serial.readline(size)

    def clean(self):
        self.__serial.flush()

    def isAvailable(self):
        return self.__serial.in_waiting


serialWriterReader = SerialWriter()



#  ..todo  b'1 3 8 1 2 8256'
