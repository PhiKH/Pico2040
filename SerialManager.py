import time

import serial
from serial import Serial


class SerialWriter(object):

    def __init__(self):
        self.__serial = Serial('COM5', 115200, timeout=0.1)

    def write(self, value):
        value += [0] # todo ???
        print('Write to Serial', value, end='\t\t')
        txs = ' '.join(map(str, value)).encode()
        self.__serial.write(txs)
        print('Read from Serial', serialWriterReader.read(100))
        time.sleep(1)

    def read(self, size):
        return self.__serial.readline(size)

    def isAvailable(self):
        return self.__serial.in_waiting

serialWriterReader = SerialWriter()



#  ..todo  b'1 3 8 1 2 8256'
