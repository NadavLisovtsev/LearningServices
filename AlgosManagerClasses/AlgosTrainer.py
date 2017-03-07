from inspect import signature
from DataManipulations.DataBuilderFactory import DataBuilderFactory
from Singleton import Singleton



class AlgosTrainer(metaclass=Singleton):
    def __init__(self):
        self._trained_algos = []

    def __safe_invoke(self, func, params):
        sig = signature(func)
        params_num = len(sig.parameters)

        if params_num == 0:
            return func()
        elif params_num == 1:
            return func(params)
        elif params_num == 2:
            return func(params[0], params[1])
        elif params_num == 3:
            return func(params[0], params[1], params[2])
        return None

    def is_algo_trained(self, algo_name):
        return algo_name in self._trained_algos

    def train_algo(self, algo, params=None):
        if self.is_algo_trained(algo.get_name()):
            return

        builder_factory = DataBuilderFactory()
        algo_name = algo.get_name()

        data_builder = builder_factory.get_builder(algo_name)
        train_data = self.__safe_invoke(data_builder.buildData, params)
        self.__safe_invoke(algo.train, train_data)

        self._trained_algos.append(algo_name)

