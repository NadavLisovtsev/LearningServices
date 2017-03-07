import numpy as np

from Config.ConfigManager import ConfigManager
from DataManipulations.DataBuilder import DataBuilder
from Learning.CrossValidators.CrossValidatorsFactory import CrossValidatorsFactory


class BestParamsFinder:

    def __init__(self):
        config = ConfigManager()
        config_section = "ParamsFinder"
        arRangeLow = int(config.get_data(config_section, "arRangeLow"))
        arRangeHigh = int(config.get_data(config_section, "arRangeHigh"))
        self._ARRange = (arRangeLow, arRangeHigh)

        gainRangeLow = int(config.get_data(config_section, "gainRangeLow"))
        gainRangeHigh = int(config.get_data(config_section, "gainRangeHigh"))
        self._gainRange = (gainRangeLow, gainRangeHigh)

        self._training = float(config.get_data("Learning", "testTrainRatio"))




    def findBestLookBack(self, compareARRange, compareGainRange, useARAsym, useGainAsym, trainTestRatio, algos):
        default_best_ratio = [1,5,5]
        bestAlgosRatio = []
        algos_num = len(algos)
        for i in range(algos_num):
            bestAlgosRatio.append(default_best_ratio)

        algosErrorsList = []
        for i in range(algos_num):
            algosErrorsList.append(np.empty((len(compareARRange)+1,len(compareGainRange) + 1)))

        firstline = [0]
        firstline.extend(compareARRange)

        for algoError in algosErrorsList:
            algoError[0] = np.asarray(firstline)

        builder = DataBuilder()
        counter = 1
        for ar in compareARRange:
            algosDiffGainErrorList = []
            for i in range(algos_num):
                algosDiffGainErrorList.append([ar])

            for g in compareGainRange:
                print("Start Calculating... AR lookBack: " + str(ar) + " Gain lookBack: " + str(g))



                (X,Y) = builder.buildDataParams(ar, g, useARAsym, useGainAsym)
                crossValidator = CrossValidatorsFactory().get_cross_validator()
                crossValidator.init(X, Y, trainTestRatio)
                meanErrosList = crossValidator.runAlgos(algos)

                for i in range(algos_num):
                    if bestAlgosRatio[i][0] > meanErrosList[i]:
                        bestAlgosRatio[i][0] = meanErrosList[i]
                        bestAlgosRatio[i][1] = ar
                        bestAlgosRatio[i][2] = g

                    algosDiffGainErrorList[i].append(meanErrosList[i])

            for i in range(algos_num):
                algosErrorsList[i][counter] = np.asarray(algosDiffGainErrorList[i])

            counter = counter +1

        return {'Best': bestAlgosRatio,
                'Errors': algosErrorsList}

    def checkAllOptions(self, algos):
        print("********** Start noAsym ************")
        noAsym = self.findBestLookBack(self._ARRange, self._gainRange, False, False, self._training, algos)
        print("********** Start onlyARAsym ************")
        onlyARAsym = self.findBestLookBack(self._ARRange, self._gainRange, True, False, self._training, algos)
        print("********* Start onlyGainAsym ***********")
        onlyGainAsym = self.findBestLookBack(self._ARRange, self._gainRange, False, True, self._training, algos)
        print("********** Start bothAsym ********")
        bothAsym = self.findBestLookBack(self._ARRange, self._gainRange, True, True, self._training, algos)
        print("****** End All Options!!! ********")

        return {'NoAsym': noAsym,
                'OnlyARAsym': onlyARAsym,
                'OnlyGainAsym': onlyGainAsym,
                'BothAsym': bothAsym}
