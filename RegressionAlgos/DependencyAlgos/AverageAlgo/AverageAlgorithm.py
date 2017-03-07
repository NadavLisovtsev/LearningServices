from RegressionAlgos.DependencyAlgos.AverageAlgo.AverageAlgorithmModel import AverageAlgorithmModel
from RegressionAlgos.DependencyAlgos.DependencyAlgo import DependencyAlgo


class AverageAlgorithm(DependencyAlgo):

    def __init__(self):
        super(AverageAlgorithm, self).__init__()
        self.name = 'AVG'
        self.model = AverageAlgorithmModel()
        self.model.init_model()


