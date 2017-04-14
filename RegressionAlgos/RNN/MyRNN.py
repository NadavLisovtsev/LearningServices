from RegressionAlgos.RNN.RNNProvider import RNNProvider
from RegressionAlgos.RegressionAlgorithm import RegressionAlgorithmBaseClass


class MyRNN(RegressionAlgorithmBaseClass):

     def __init__(self):
         super(MyRNN, self).__init__()
         self.name = 'RNN'
         self._look_back = 3
         self.model = RNNProvider()

     def calcError(self, testX, testY,  compareFunc):
         return self.model.calc_error(testX, testY)

     def   get_look_back(self):
         return self._look_back