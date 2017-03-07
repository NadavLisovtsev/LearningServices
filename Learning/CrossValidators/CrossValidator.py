import math
import numpy as np

from Config.ConfigManager import ConfigManager


class CrossValidator:

    def init(self, X, Y, ratio):
        config = ConfigManager()

        self.X = X
        self.Y = Y
        self.iters = int(config.get_data("CrossValidator", "iterations"))
        self.ratio = ratio


    def runAlgos(self, algosList):
        resultsList = []
        for algo in algosList:
            errorsSum = 0.0
            for i in range(self.iters):
                (trainX, trainY, testX, testY) = self.buildTrainTest()
                algo.train(trainX, trainY)
                errorsSum += algo.calcError(testX, testY, lambda p, t: np.mean([math.fabs(x) for x in (p-t)]))
                print(" " + str(i) + ",", end = "")
            resultsList.append(errorsSum/self.iters)
        print("")
        return resultsList