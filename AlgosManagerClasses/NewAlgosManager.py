from Config.ConfigManager import ConfigManager
from DTOs.GameData import GameData
from DataManipulations.DataBuilder import DataBuilder
from Learning.ParamsManager import ParamsManager
from RegressionAlgos.MyNN import MyNN
from RegressionAlgos.MyRF import RandomForest
from RegressionAlgos.MySVM import MySVM
from RegressionAlgos.RNN.MyRNN import MyRNN
from RegressionAlgos.RegressionAlgorithm import RegressionAlgorithmBaseClass
from Singleton import Singleton


class NewAlgosManager(metaclass=Singleton):
    def __init__(self):
        self._config = ConfigManager()
        self._conf_section = 'RegressionService'

        self._algos_names_dict = {
                'NN': MyNN(),
                'SVM': MySVM(),
                'RF': RandomForest(),
                'RNN': MyRNN()
        }
        self.algos = {}
        self.params = {}

    def init_algos(self):
        algos_names = self._get_algos_names()
        params_manager = ParamsManager()
        for algo_name in algos_names:
            self.algos[algo_name] = self._algos_names_dict[algo_name]
            self.params[algo_name] = params_manager.get_params_for_algo(algo_name)

    def train_algos(self, users_dict):
        for algo_name in self.algos.keys():
            self.train_algo(self.algos[algo_name], users_dict)

    def train_algo(self, algo: RegressionAlgorithmBaseClass, users_dict):
        params = self.params[algo.get_name()]
        data_builder = DataBuilder()
        (X, Y) = data_builder.build_xy_data(users_dict, params)
        algo.train(X, Y)

    def run_algo(self, algo_name, game_data: GameData):
        algo = self.algos[algo_name]
        params = self.params[algo_name]
        data_builder = DataBuilder()
        X = data_builder.build_predict_data(game_data, params)
        return algo.get_prediction(X)

    def _get_algos_names(self):
        names = self._config.get_data(self._conf_section, 'algos')
        return names.split(',')
