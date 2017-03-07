import numpy as np
from sklearn.linear_model import LinearRegression
from RegressionAlgos.DependencyAlgos.DependencyAlgoModel import DependencyAlgoModel


class LinearRegressionModel(DependencyAlgoModel):

    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self._regression_model = LinearRegression()

    def get_config_section(self):
        return "LinearRegression"


    def fit(self, trainX, trainY):

        regressionX = []
        regressionX.append([self.get_algo_results(X) for X in trainX])

        regressionX = np.asarray(regressionX)
        trainY = np.asarray(trainY)

        self._regression_model.fit(regressionX, trainY)

    # X: X[0] = ars, X[1] = Gains
    def predict(self, X):
        algo_results = self.get_algo_results(X)
        return self._regression_model.predict(np.asarray(algo_results))






