from RegressionAlgos.DependencyAlgos.DependencyAlgo import DependencyAlgo
from RegressionAlgos.DependencyAlgos.LinearRegression.LinearRegressionModel import LinearRegressionModel

class MyLR(DependencyAlgo):
    def __init__(self):
        super(MyLR, self).__init__()
        self.name = 'LR'
        self.model = LinearRegressionModel()
        self.model.init_model()


