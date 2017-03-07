from RegressionAlgos.RegressionAlgorithm import RegressionAlgorithmBaseClass


class DependencyAlgo(RegressionAlgorithmBaseClass):
    def __init__(self):
        super(DependencyAlgo, self).__init__()

    def get_look_back(self):
         return self.model.get_look_back()