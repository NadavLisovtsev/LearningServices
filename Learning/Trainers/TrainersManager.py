from Learning.Trainers.DefaultTrainer import DefaultTrainer
from Learning.Trainers.RNNTrainer import RNNTrainer
from Learning.Trainers.TrainerRunner import TrainerRunner


class TrainerManager:
    def __init__(self):
          self._trainers_dict = {
            'RNN': RNNTrainer(),
            'Default': DefaultTrainer()
        }

    def __get_trainer(self, algo_name):
        return self._trainers_dict[algo_name] if algo_name in self._trainers_dict.keys() \
            else self._trainers_dict["Default"]

    def get_trainer_runner(self, algos):
        runner = TrainerRunner()
        for algo in algos:
            runner.add_algos(self.__get_trainer(algo.get_name()), [algo])

        return runner


    def get_trainer_name_by_algo(self, algo_name):
        return self.__get_trainer(algo_name).__class__.__name__

