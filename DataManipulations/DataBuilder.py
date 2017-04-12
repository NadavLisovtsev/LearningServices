import numpy as np

from DTOs.AllFeaturesParams import AllFeaturesParams
from DTOs.GameData import GameData
from DTOs.RawGameData import RawGameData
from DataManipulations.DAL import DAL
from DataManipulations.DataOrganizer import DataOrganizer
from Features.FeaturesManager import FeaturesManager


class DataBuilder:

    def build_xy_data(self, users_dict, features_params: AllFeaturesParams):
        features_manager = FeaturesManager()
        features = features_manager.get_active_features()
        y_feature = features_manager.get_y_feature()
        features.append(y_feature)



        user_count = 0
        print("total users: " + str(len(users_dict.keys())))
        for user in users_dict.keys():
            raw_data = RawGameData()
            for feature in features:
                game_data = users_dict[user]
                params = features_params.get_feature_params(feature.get_name())
                raw_data.merge_raw_game_data(feature.get_raw_data_from_game(game_data, params))
            (x, y) = raw_data.get_XY_matrix()
            if user_count == 0:
                X = x
                Y = y
            else:
                print(np.shape(X), np.shape(x))
                if np.shape(X)[1] == np.shape(x)[1]:
                    X = np.concatenate((X, x))
                    Y = np.concatenate((Y, y))
            user_count += 1
            print("Done with user: " + user + ", Number: " + str(user_count))
        return X, Y


"""
    def getARsGains(self):
        d = DAL()

        users = d.getAllUsers()
        ARsDict = {}
        gainsDict = {}
        for user in users:
            ARs = []
            gains = []
            ARandEarn = d.getARandEarnPercentForUser(user)
            for i in ARandEarn:
                ARs.append(i[0])
                gains.append(i[1])
            ARsDict[user] = ARs
            gainsDict[user] = gains

        return (ARsDict, gainsDict)

    def buildData(self, params):
        return self.buildDataParams(params['ARLookBack'], params['GainLookBack'], params['useARAsymAverage'], params['useGainAsymAverage'])

    def buildDataParams(self, ARLookback, gainLookBack, useARAsymAvg, useGainAsymAvg):

        (ARsDict, gainsDict) = self.getARsGains()

        organizer = DataOrganizer(ARsDict, gainsDict)
        (X,Y) = organizer.organizeData(ARLookback, gainLookBack, useARAsymAvg, useGainAsymAvg)

        return (X,Y)

    def buildTrainTestFunc(self, X, Y, trainTestRatio):
        lenX = len(X)
        lenY = len(Y)

        trainX = X[0:round(lenX * trainTestRatio)]
        trainY = Y[0:round(lenY * trainTestRatio)]

        testX = X[round(lenX * trainTestRatio) + 1:]
        testY = Y[round(lenY * trainTestRatio) + 1:]

        return (trainX, trainY, testX, testY)
"""
