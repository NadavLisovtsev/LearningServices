from AlgosManagerClasses.AlgosKeeper import AlgosKeeper
from DataManipulations.DataBuilder import DataBuilder

class LRDataBuilder:

    def __init__(self):
        algos_keeper = AlgosKeeper()
        self.look_back = algos_keeper.get_algo_look_back("LR")

    def buildData(self):
        data_builder = DataBuilder()
        (ARsDict, gainsDict) = data_builder.getARsGains()

        trainX = []
        trainY = []
        for user in ARsDict.keys():
            ars = ARsDict[user]
            gains = gainsDict[user]
            user_trainX, user_trainY = self.build_user_data(ars, gains)
            trainX.extend(user_trainX)
            trainY.extend(user_trainY)

        return trainX, trainY

    def build_user_data(self, ars, gains):
        start_index = self.look_back

        x = []
        y = []
        for i in range(start_index, len(ars)-1):
            x.append(([ars[:i]],[gains[:i]]))
            y.append(ars[i+1])
        return x, y

