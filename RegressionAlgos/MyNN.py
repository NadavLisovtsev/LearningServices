from sklearn.neural_network import MLPRegressor
from RegressionAlgos.RegressionAlgorithm import RegressionAlgorithmBaseClass

class MyNN(RegressionAlgorithmBaseClass):

    def __init__(self):
        super(MyNN, self).__init__()
        self.name = 'NN'
        self.model = MLPRegressor()
