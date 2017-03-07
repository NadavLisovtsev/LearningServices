from DataManipulations.DataBuilder import DataBuilder


class RNNDataBuilder:

    def buildData(self):

        data_builder = DataBuilder()
        (ARsDict, gainsDict) = data_builder.getARsGains()

        variableDataAR = self.__organizeVariableDataRNN(ARsDict)
        variableDataGain = self.__organizeVariableDataRNN(gainsDict)
        YData = self.__getYForRNN(ARsDict)

        return (variableDataAR, variableDataGain), YData

    def __organizeVariableDataRNN(self, variableDict):
        variableMatrix = []
        for user in variableDict:
            userData = variableDict[user]
            if len(userData) == 20:
                variableMatrix.append(userData[1:])
        return variableMatrix

    def __getYForRNN(self, variableDict):
        variableMatrix = []
        for user in variableDict:
            userData = variableDict[user]
            if len(userData) == 20:
                variableMatrix.append(userData[:-1])
        return variableMatrix


        

