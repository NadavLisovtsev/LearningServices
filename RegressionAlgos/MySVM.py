from sklearn import svm
from RegressionAlgos.RegressionAlgorithm import RegressionAlgorithmBaseClass


class MySVM(RegressionAlgorithmBaseClass):
    def __init__(self):
        super(MySVM, self).__init__()
        self.name = 'SVM'
        self.model = svm.SVR()

