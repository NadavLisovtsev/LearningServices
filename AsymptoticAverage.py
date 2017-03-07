from APIs.UtilitiesAPI import UtilitiesAPI


class AsymptoticAverage:
    def calcAverage(self, l):
        server = UtilitiesAPI()
        return server.calcAsymptoticAverage(l)

    def addValToAverage(self, value, average):
        server = UtilitiesAPI()
        return server.AddValueToAsymptoticAverage(value, average)
