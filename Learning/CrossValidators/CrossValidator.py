import math
import numpy as np

from Config.ConfigManager import ConfigManager
from DTOs.CrossValidationResults import CrossValidationResults
from DTOs.GameData import GameData
from DTOs.RawGameData import RawGameData
from RegressionAlgos.RegressionAlgorithm import RegressionAlgorithmBaseClass


class CrossValidator:

    def init(self, X, Y, ratio):
        config = ConfigManager()

        self.X = X
        self.Y = Y
        self.iters = int(config.get_data("CrossValidator", "iterations"))
        self.ratio = ratio

    def run_algo(self, algo: RegressionAlgorithmBaseClass) -> CrossValidationResults:
        errors = CrossValidationResults()
        for i in range(self.iters):
            (trainX, trainY, testX, testY) = self.buildTrainTest()
            algo.train(trainX, trainY)
            errors.add_error(algo.calcError(testX, testY, lambda p, t: np.mean([math.fabs(x) for x in (p-t)])))
           # print(" " + str(i) + ",", end="")
            print(" " + str(i))
        return errors

    def _buildTrainTest(self, game_data: GameData, params) -> RawGameData:
        raise Exception("Not Implemented!! Feature class has no Implementation to this method")

