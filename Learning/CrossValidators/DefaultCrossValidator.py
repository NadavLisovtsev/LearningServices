import numpy as np

from Learning.CrossValidators.CrossValidator import CrossValidator


class DefaultCrossValidator(CrossValidator):

    def buildTrainTest(self):
        X = self.X
        Y = self.Y
        lenX = len(X)
        lenY = len(Y)
        trainTestRatio = self.ratio



        #randomizing the data
        (r, c) = np.shape(X)
        Y = np.asarray(Y).reshape((lenY, 1))

        M = np.concatenate((X, Y), axis=1)
        np.random.shuffle(M)

        X = M[:, range(c)]
        Y = M[:, [c]]
        Y = Y.reshape(lenY)
        #end randomizing data


        trainX = X[0:round(lenX * trainTestRatio)]
        trainY = Y[0:round(lenY * trainTestRatio)]

        testX = X[round(lenX * trainTestRatio) + 1:]
        testY = Y[round(lenY * trainTestRatio) + 1:]

        return (trainX, trainY, testX, testY)

