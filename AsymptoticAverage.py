from APIs.UtilitiesAPI import UtilitiesAPI
from APIs.UtilitiesZMQAPI import UtilitiesZMQAPI


class AsymptoticAverage:
    def __init__(self):
        self._server = UtilitiesZMQAPI()

    def calcAverage(self, l):
        return self._server.calcAsymptoticAverage(l)

    def addValToAverage(self, value, average):
        return self._server.AddValueToAsymptoticAverage(value, average)
