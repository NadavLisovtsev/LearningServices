import numpy as np

from Config.ConfigManager import ConfigManager
from DataManipulations.RNN.RNNDataBuilder import RNNDataBuilder
from Learning.CrossValidators.CrossValidator import CrossValidator
from Learning.CrossValidators.CrossValidatorsFactory import CrossValidatorsFactory


class RNNTrainer():
    def train(self, algos):
        config = ConfigManager()
        train_test_ratio = float(config.get_data("Learning", "testTrainRatio"))

        data_builder = RNNDataBuilder()
        ((var1, var2), Y) = data_builder.buildData()
       #X = np.column_stack((var1, var2))

        factory = CrossValidatorsFactory()
        cross_validator = factory.get_cross_validator("RNN")
        cross_validator.init((var1, var2), Y, train_test_ratio)

        return cross_validator.runAlgos(algos)
