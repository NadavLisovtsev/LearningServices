from APIs.RAPI import RAPI
from Config.ConfigManager import ConfigManager
from DataManipulations.RNN.RNNDataBuilder import RNNDataBuilder
from Output.OutputManager import OutputManager


class RNNProvider():
    def __init__(self):
        config = ConfigManager()
        config_section = "RNN"

        self._training_script = config.get_data(config_section, "trainingScript")
        self._prediction_script = config.get_data(config_section, "predictionScript")
        self._test_script = config.get_data(config_section, "testScript")

        output_manager = OutputManager()
        self.data_printer = output_manager.get_printer("RNN")


        self.RProxy = RAPI()
        self._is_trained = False
        self._error = None

    def fit(self, trainX, trainY):
        self.data_printer.save_train_data(trainX, trainY)
        self._train_error = self.RProxy.run_script(self._training_script)
        self._is_trained = True

    def predict(self, X):
        self.data_printer.save_prediction_data(X)
        return self.RProxy.run_script(self._prediction_script)

    def calc_error(self, testX, testY):
        self.data_printer.save_test_data(testX, testY)
        return float(self.RProxy.run_script(self._test_script))




