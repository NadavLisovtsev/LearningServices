from DataManipulations.DAL import DAL
from DataManipulations.DataOrganizer import DataOrganizer


class DataBuilder:

    def getARsGains(self):
        d = DAL()

        users = d.getAllUsers()
        ARsDict = {}
        gainsDict = {}
        for user in users:
            ARs = []
            gains = []
            ARandEarn = d.getARandEarnPercentForUser(user)
            for i in ARandEarn:
                ARs.append(i[0])
                gains.append(i[1])
            ARsDict[user] = ARs
            gainsDict[user] = gains

        return (ARsDict, gainsDict)

    def buildData(self, params):
        return self.buildDataParams(params['ARLookBack'], params['GainLookBack'], params['useARAsymAverage'], params['useGainAsymAverage'])

    def buildDataParams(self, ARLookback, gainLookBack, useARAsymAvg, useGainAsymAvg):

        (ARsDict, gainsDict) = self.getARsGains()

        organizer = DataOrganizer(ARsDict, gainsDict)
        (X,Y) = organizer.organizeData(ARLookback, gainLookBack, useARAsymAvg, useGainAsymAvg)

        return (X,Y)

    def buildTrainTestFunc(self, X, Y, trainTestRatio):
        lenX = len(X)
        lenY = len(Y)

        trainX = X[0:round(lenX * trainTestRatio)]
        trainY = Y[0:round(lenY * trainTestRatio)]

        testX = X[round(lenX * trainTestRatio) + 1:]
        testY = Y[round(lenY * trainTestRatio) + 1:]

        return (trainX, trainY, testX, testY)
