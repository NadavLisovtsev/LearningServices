import numpy as np
from AsymptoticAverage import AsymptoticAverage


class DataOrganizer:
    def __init__(self, ARsDict=None, gainsDict=None):
        self.ARsDict = ARsDict
        self.gainsDict = gainsDict
        self.minGainOffset = 5
        self.minAROffset = 5

    def __extract_best_params(self, params):
        return (params['ARLookBack'], params['GainLookBack'], params['useARAsymAverage'], params['useGainAsymAverage'])

    def organize_prediction_data(self, AR, Gain, params):

        ARLookBack,  gainLookBack,  useARAsymAverage, useGainAsymAverage = self.__extract_best_params(params)

        asymAvg = AsymptoticAverage()

        features = []
        ARs_offset = len(AR) - ARLookBack
        gain_offset = len(Gain) - gainLookBack
        if ARs_offset < 0 or gain_offset < 0:
            raise Exception("Not enough values!! the ARs_offset is: " + str(ARs_offset) + " the gain offset is: " + str(gain_offset))

        features.extend(AR[ARs_offset:])
        features.extend(Gain[gain_offset:])

        if useGainAsymAverage and len(Gain[:len(Gain) - gainLookBack]) > 0:
                avg = asymAvg.calcAverage(Gain[:len(Gain) - gainLookBack])
                features.append(avg)
        if useARAsymAverage and len(AR[:len(AR) - ARLookBack]) > 0:
                avg = asymAvg.calcAverage(AR[:len(AR) - ARLookBack])
                features.append(avg)

        return features



    def organizeUserData(self, userAR, userGain, gainLookBack, ARLookBack, useGainAsymAverage, useARAsymAverage):
        gainOffset = max(self.minGainOffset, gainLookBack)
        AROffset = max(self.minAROffset, ARLookBack)
        offset = max(gainOffset, AROffset)
        if useGainAsymAverage or useARAsymAverage:
            offset = offset + 1

        relevantGains = userGain[offset:]
        relevantARs = userAR[offset:]

        if len(relevantGains) != len(relevantARs):
            raise Exception("Wrong Length!! AR: " + str(len(relevantARs)) + ", gains: " + str(len(relevantGains)))

        relevantLen = len(relevantGains)
        featuresNum = gainLookBack + ARLookBack + (1 if useGainAsymAverage else 0) + (1 if useARAsymAverage else 0)
        X = np.empty((relevantLen, featuresNum), 'float64')
        Y = np.empty(relevantLen, 'float64')

        asymAvg = AsymptoticAverage()
        for relevantIndex in range(relevantLen):
            actualIndex = relevantIndex + offset
            features = []
            features.extend(userAR[actualIndex - ARLookBack:actualIndex])
            features.extend(userGain[actualIndex - gainLookBack:actualIndex])
            if useGainAsymAverage:
                avg = asymAvg.calcAverage(userGain[:actualIndex - gainLookBack])
                features.append(avg)
            if useARAsymAverage:
                avg = asymAvg.calcAverage(userAR[:actualIndex - ARLookBack])
                features.append(avg)

            Y[relevantIndex] = relevantARs[relevantIndex]
            X[relevantIndex] = np.asarray(features)
        return (X, Y)

    def organizeData(self, gainLookBack, ARLookBack, useGainAsymAverage, useARAsymAverage):
        X = []
        Y = []
        for user in self.ARsDict:
            ARs = self.ARsDict[user]
            gains = self.gainsDict[user]
            (userX, userY) = self.organizeUserData(ARs, gains, gainLookBack, ARLookBack, useGainAsymAverage, useARAsymAverage)
            X.extend(userX)
            Y.extend(userY)
        return (X, Y)
