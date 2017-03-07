from AlgosManagerClasses.AlgosKeeper import AlgosKeeper
from AlgosManagerClasses.AlgosRunner import AlgosRunner
from AlgosManagerClasses.AlgosTrainer import AlgosTrainer
from Config.ConfigManager import ConfigManager


class DependencyAlgoModel:

    def __init__(self):

        self._algos_keeper = AlgosKeeper()
        self._algos_trainer = AlgosTrainer()
        self._algos_runner = AlgosRunner()

    def init_model(self):
        self.__init_dependencies()
        self.__init_algos()
        self.__train_algos()

    def __init_dependencies(self):
        config = ConfigManager()
        config_section = self.get_config_section()
        self._dependencies = config.get_data(config_section, "Dependencies").split(',')


    def __init_algos(self):
         for algo_name in self._dependencies:
            if not self._algos_keeper.is_algo_initialized(algo_name):
                self._algos_keeper.init_algo(algo_name)

    def __train_algos(self):
        for algo_name in self._dependencies:
            if not self._algos_trainer.is_algo_trained(algo_name):
                algo = self._algos_keeper.get_algo(algo_name)
                params = self._algos_keeper.get_algo_params(algo_name)
                self._algos_trainer.train_algo(algo, params)

    def get_algo_results(self, X):
        results = []
        for algo_name in self._dependencies:
            algo = self._algos_keeper.get_algo(algo_name)
            params = self._algos_keeper.get_algo_params(algo_name)
            results.append(float(self._algos_runner.run_algo(algo, X[0], X[1], params)))
        print(results)
        return results

    def get_look_back(self):
        return max([self._algos_keeper.get_algo_look_back(algo_name) for algo_name in self._dependencies])

    def get_config_section(self):
        raise Exception("Method ' __get_config_section' Not Implemented!!")
