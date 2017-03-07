import json
import requests

from Config.ConfigManager import ConfigManager


class UtilitiesAPI:
    def __init__(self):
        self._config = ConfigManager()
        self._config_section = "UtilitiesAPI"
        self.serverUrl = self._config.get_data(self._config_section, "serverUrl")

    def sendRequestToService(self, methodName, dataDict):
        url = self.serverUrl + methodName
        data = json.dumps(dataDict)
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, data=data, headers=headers)
        result = response.json()
        return result[methodName + "Result"]

    def calcAsymptoticAverage(self, l):
        return self.sendRequestToService("CalcAsymptoticAverage", {"values": l})

    def AddValueToAsymptoticAverage(self, value, average):
        return self.sendRequestToService("AddValueToAsymptoticAverage", {"value": value, "average": average})

