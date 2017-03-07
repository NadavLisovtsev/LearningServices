from Learning.BestParamsFinder import BestParamsFinder


class DefaultTrainer:

    def train(self, algos):
        params_checker = BestParamsFinder()
        return params_checker.checkAllOptions(algos)
