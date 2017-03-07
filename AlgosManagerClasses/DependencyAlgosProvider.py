from RegressionAlgos.DependencyAlgos.AverageAlgo.AverageAlgorithm import AverageAlgorithm
from RegressionAlgos.DependencyAlgos.LinearRegression.MyLR import MyLR
from Singleton import Singleton


class DependencyAlgosProvider(metaclass=Singleton):
     def __init__(self):
         self._algos_names_dict = {
                'AVG': AverageAlgorithm(),
                'LR': MyLR(),
         }

     def get_algo(self, algo_name):
         return self._algos_names_dict[algo_name]