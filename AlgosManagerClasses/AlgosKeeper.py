import json
from inspect import ismethod

from Config.ConfigManager import ConfigManager
from Singleton import Singleton
from RegressionAlgos.MyNN import MyNN
from RegressionAlgos.MyRF import RandomForest
from RegressionAlgos.MySVM import MySVM
from RegressionAlgos.RNN.MyRNN import MyRNN

class AlgosKeeper(metaclass=Singleton):
    def __init__(self):
         self._algos_names_dict = {
                'NN': MyNN(),
                'SVM': MySVM(),
                'RF': RandomForest(),
                'RNN': MyRNN()
         }
         self._config = ConfigManager()
         self._conf_section = 'RegressionService'

         self._algos = {}
         self._params = {}
         self._initilaized_algos = []

         self._best_params = self.__get_best_params()

    def __get_best_params(self):
        file_name = self._config.get_data(self._conf_section, 'bestParamsFile')
        with open(file_name, 'r') as f:
            data = f.read()
        return json.loads(data)

    def __add_best_params(self, algo_name):
        self._params[algo_name] = self._best_params[algo_name]

    def __default_look_back(self, algo_name):
        params = self._params[algo_name]
        return max(params['GainLookBack'], params['ARLookBack'])

    def init_algo(self, algo_name):
        print("initialized algo: " + algo_name)
        if not self.is_algo_initialized(algo_name):
            self._algos[algo_name] = self._algos_names_dict[algo_name]
            self.__add_best_params(algo_name)
            self._initilaized_algos.append(algo_name)

    def is_algo_initialized(self, algo_name):
        return algo_name in self._initilaized_algos

    def get_algo(self, name):
        return self._algos[name]

    def get_initialized_algos(self):
        return self._algos

    def get_algo_params(self, algo_name):
        return self._params[algo_name]

    def add_algo(self, algo, params):
        self._algos[algo.get_name()] = algo
        self._initilaized_algos.append(algo.get_name())
        self._params[algo.get_name()] = params

    def get_algo_look_back(self, algo_name):
        algo = self._algos[algo_name]
        return algo.get_look_back() if hasattr(algo, 'get_look_back') and ismethod(getattr(algo, 'get_look_back')) \
            else self.__default_look_back(algo_name)
