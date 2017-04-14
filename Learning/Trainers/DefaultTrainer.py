from Learning.BestParamsFinder import BestParamsFinder
from RegressionAlgos.RegressionAlgorithm import RegressionAlgorithmBaseClass


class DefaultTrainer:

    def train(self, algos):
        results_dict = {}
        for algo in algos:
            results_dict[algo.get_name()] = self.train_algo(algo)
        return results_dict

    def train(self, algos):
        params_checker = BestParamsFinder()
        return params_checker.checkAllOptions(algos)
