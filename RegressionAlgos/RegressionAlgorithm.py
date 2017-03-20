import csv

class RegressionAlgorithmBaseClass:

    def __init__(self):
        self.model = None
        self.name = None

    def train(self, trainX, trainY):
        """
        with open('trainX.csv', 'w') as f:
            writer = csv.writer(f, delimiter=',')
            for row in trainX:
                writer.writerow(row)

        with open('trainY.csv', 'w') as f:
            writer = csv.writer(f, delimiter=',')
            for row in trainY:
                writer.writerow([row])
        """

        self.model.fit(trainX, trainY)
        return self.model

    def get_prediction(self, X):
        predictedY = self.model.predict(X)

        try:
            result = predictedY[0]
        except TypeError:
            result = predictedY

        return result

    def calcError(self, testX, testY,  compareFunc):
        predictedY = self.model.predict(testX)
        return compareFunc(predictedY, testY)

    def get_name(self):
        return self.name

