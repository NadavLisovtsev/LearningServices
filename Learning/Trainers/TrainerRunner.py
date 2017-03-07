class TrainerRunner:

    def __init__(self):
        self._trainers_dict = {}

    def add_algos(self, trainer, algos):
        if trainer.__class__.__name__ in self._trainers_dict.keys():
            self._trainers_dict[trainer.__class__.__name__][1].extend(algos)
        else:
            self._trainers_dict[trainer.__class__.__name__] = (trainer, algos)

    def run_trainer(self, trainer_name):
        trainer = self._trainers_dict[trainer_name][0]
        algos = self._trainers_dict[trainer_name][1]

        return trainer.train(algos)

    def get_all_trainers(self):
        return [t[0] for t in self._trainers_dict.values()]

    def run_all_trainers(self):
        results_dict = {}
        trainers = self.get_all_trainers()
        for trainer in trainers:
            result = self.run_trainer(trainer.__class__.__name__)
            results_dict[trainer.__class__.__name__] = result
        return results_dict