from sklearn.ensemble import RandomForestRegressor
from RegressionAlgos.RegressionAlgorithm import RegressionAlgorithmBaseClass


class RandomForest(RegressionAlgorithmBaseClass):

     def __init__(self):
         super(RandomForest, self).__init__()
         self.name = 'RF'
         self.model = RandomForestRegressor(n_estimators=100)
