from RegressionAlgos.DependencyAlgos.DependencyAlgoModel import DependencyAlgoModel


class AverageAlgorithmModel(DependencyAlgoModel):

    def __init__(self):
        super(AverageAlgorithmModel, self).__init__()

    def get_config_section(self):
        return "AverageAlgorithm"

    def fit(self, trainX, trainY):
        pass

    # X: X[0] = ars, X[1] = Gains
    def predict(self, X):
        algo_results = self.get_algo_results(X)
        return sum(algo_results) / float(len(algo_results))





