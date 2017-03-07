from AlgosManagerClasses.AlgosKeeper import AlgosKeeper
from AlgosManagerClasses.AlgosRunner import AlgosRunner
from AlgosManagerClasses.AlgosTrainer import AlgosTrainer
from AlgosManagerClasses.DependencyAlgosProvider import DependencyAlgosProvider
from Config.ConfigManager import ConfigManager
from Singleton import Singleton


class AlgosManager(metaclass=Singleton):
    def __init__(self):
        self._config = ConfigManager()
        self._conf_section = 'RegressionService'

        self._keeper = AlgosKeeper()
        self._trainer = AlgosTrainer()
        self._runner = AlgosRunner()
        self._dependency_algos_provider = DependencyAlgosProvider()

    # PRIVATE METHODS

    def __get_algos_names(self):
        names = self._config.get_data(self._conf_section, 'algos')
        return names.split(',')

    def __get_dependency_algos_names(self):
        return self._config.get_data(self._conf_section, "dependencyAlgos").split(',')

    # END PRIVATE METHODS

    def init_algos(self):
        algos_names = self.__get_algos_names()
        for algo_name in algos_names:
            if not self._keeper.is_algo_initialized(algo_name):
                self._keeper.init_algo(algo_name)
        dependency_algo_names = self.__get_dependency_algos_names()
        for name in dependency_algo_names:
            algo = self._dependency_algos_provider.get_algo(name)
            self._keeper.add_algo(algo, None)

    def train_algos(self):
        algos = self._keeper.get_initialized_algos()
        for algo_name in algos.keys():
            if not self._trainer.is_algo_trained(algo_name):
                params = self._keeper.get_algo_params(algo_name)
                self._trainer.train_algo(algos[algo_name], params)

    def run_algo(self, algo_name, ars, gains):
        algo = self._keeper.get_algo(algo_name)
        params = self._keeper.get_algo_params(algo_name)
        return self._runner.run_algo(algo, ars, gains, params)

    def get_algo_look_back(self, algo_name):
       return self._keeper.get_algo_look_back(algo_name)

