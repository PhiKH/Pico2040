from serial import Serial


class SerialWriter(object):

    def __init__(self):
        self.__serial = Serial('/dev/ttyACM0', 115200, timeout=0.1)

    def write(self, command, value):
        if type(value) == list:
            for byte in value:
                self.__write(command, str(byte))
        else:
            self.__write(command, str(value))

    # todo
    def __write(self, command, value):
        res = command + ' ' + value
        if type(res) == int:
            self.__serial.write(str(res).encode())
        elif type(res) == str:
            self.__serial.write(res.encode())

    def read(self, size):
        return self.__serial.readline(size)


serialWriterReader = SerialWriter()
