from SerialManager import serialWriterReader

AD56X4_COMMAND_WRITE_INPUT_REGISTER = 0b00000000
AD56X4_COMMAND_UPDATE_DAC_REGISTER = 0b00001000
AD56X4_COMMAND_WRITE_INPUT_REGISTER_UPDATE_ALL = 0b00010000
AD56X4_COMMAND_WRITE_UPDATE_CHANNEL = 0b00011000
AD56X4_COMMAND_POWER_UPDOWN = 0b00100000
AD56X4_COMMAND_RESET = 0b00101000
AD56X4_COMMAND_SET_LDAC = 0b00110000
AD56X4_COMMAND_REFERENCE_ONOFF = 0b00111000
AD56X4_CHANNEL_A = 0b00000000
AD56X4_CHANNEL_B = 0b00000001
AD56X4_CHANNEL_C = 0b00000010
AD56X4_CHANNEL_D = 0b00000011
AD56X4_CHANNEL_ALL = 0b00000111
AD56X4_SETMODE_INPUT = AD56X4_COMMAND_WRITE_INPUT_REGISTER
AD56X4_SETMODE_INPUT_DAC = AD56X4_COMMAND_WRITE_UPDATE_CHANNEL
AD56X4_SETMODE_INPUT_DAC_ALL = AD56X4_COMMAND_WRITE_INPUT_REGISTER_UPDATE_ALL
AD56X4_POWERMODE_NORMAL = 0b00000000
AD56X4_POWERMODE_POWERDOWN_1K = 0b00010000
AD56X4_POWERMODE_POWERDOWN_100K = 0b00100000
AD56X4_POWERMODE_TRISTATE = 0b00110000


class AD5664:
    def __init__(self, port):
        self.__numPort = port
        self.__bitPerWord = 8
        self.__chpa = 1
        self.__cpol = 0
        self.__serial = serialWriterReader

    def __getSettings(self):
        return [self.__numPort, self.__bitPerWord, self.__chpa, self.__cpol]

    def getPortNumber(self):
        return self.__numPort

    def _send(self, value):
        self.__serial.write([20] + self.__getSettings() + value)

    def __writeMsg(self, cmd, adr, data):
        data_high = data >> 8
        data_low = data & 0x00ff
        self._send([(cmd & 0b00111000) | (adr & 0b00000111), data_high, data_low])

    def setChannel(self, mode, ch, value):
        if mode == AD56X4_SETMODE_INPUT or mode == AD56X4_SETMODE_INPUT_DAC or mode == AD56X4_SETMODE_INPUT_DAC_ALL:
            self.__writeMsg(mode, ch, value)

    def updateChannel(self, ch):
        self.__writeMsg(AD56X4_COMMAND_UPDATE_DAC_REGISTER, ch, 0)

    def powerUpDown(self, powerMode, channel):
        self.__writeMsg(AD56X4_COMMAND_POWER_UPDOWN, 0, int(((0b00110000 & powerMode) | (0b00001111 & channel))))

    def reset(self, full):
        self.__writeMsg(AD56X4_COMMAND_RESET, 0, int(full))

    def setInputMode(self, channel):
        self.__writeMsg(AD56X4_COMMAND_SET_LDAC, 0, int(channel))

    def useInternalRef(self, yesno):
        self.__writeMsg(AD56X4_COMMAND_REFERENCE_ONOFF, 0, int(yesno))
