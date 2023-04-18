import time

from SerialManager import serialWriterReader

WAVE_LIST = ['SIN', 'SQU', 'TRI']
waveforms = [0x2000, 0x2028, 0x2002]


class WaveGen:
    def __init__(self, port, freq=None):
        self.__numPort = port
        self.__bitPerWord = 8
        self.__chpa = 1
        self.__cpol = 1
        self.__spiWriter = serialWriterReader

        self.__waveForm = 0x2000
        if freq is not None:
            self.__freq = freq
        else:
            self.__freq = 1000
        self.__isWorked = False
        self.clk_freq = 25.0e6
        self._send([32, 64]) # reset

    def __getSettings(self):
        return [self.__numPort, self.__bitPerWord, self.__chpa, self.__cpol]

    @staticmethod
    def __getBytes(integer):
        return divmod(integer, 0x100)

    def _send(self, value):
        self.__spiWriter.write([1] + self.__getSettings() + value)

    def setFreq(self, freq):
        self.__freq = freq

    def stateOn(self, freq):
        self.__isWorked = True
        self.send_f(freq)

    def setWave(self, formIndex):
        self.__waveForm = waveforms[formIndex]

    def stateOff(self):
        self.__isWorked = False
        self._send([0x2040])

    def getForm(self):
        return WAVE_LIST[waveforms.index(self.__waveForm)]

    def getState(self):
        return self.__isWorked

    def send_f(self, f):
        if f is not None:
            self.__freq = f
        flag_b28 = 1 << 13
        flag_freq = 1 << 14
        scale = 1 << 28
        n_reg = int(self.__freq * scale / self.clk_freq)
        n_low = n_reg & 0x3fff
        n_hi = (n_reg >> 14) & 0x3fff

        a, b = self.__getBytes(flag_freq | n_low)
        self._send([a, b])
        a, b = self.__getBytes(flag_freq | n_hi)
        self._send([a, b])
        a, b = self.__getBytes(self.__waveForm)
        self._send([a, b])

    def getPortNumber(self):
        return self.__numPort