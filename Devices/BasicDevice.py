from SerialManager import serialWriterReader


class BasicDevice(object):

    def __init__(self):
        self._numPort = None
        self._bitPerWord = None
        self._chpa = None
        self._cpol = None
        self._spiWriter = serialWriterReader

    def _getSettings(self):
        return [self._numPort, self._bitPerWord, self._chpa, self._cpol]