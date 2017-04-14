from Learning.CrossValidators.CrossValidator import CrossValidator
import numpy as np


class RNNCrossValidator(CrossValidator):

    def _buildTrainTest(self):
        var1 = self.X[0]
        var2 = self.X[1]
        Y = self.Y

        rows_num = np.shape(Y)[0]
        columns_num = np.shape(Y)[1]

        indexes = np.asarray(range(0,rows_num))

        #randomizing the data
        np.random.shuffle(indexes)

        shuffled_var1 = np.empty((rows_num, columns_num))
        shuffled_var2 = np.empty((rows_num, columns_num))
        shuffled_Y = np.empty((rows_num, columns_num))

        shuffled_index = 0
        for i in indexes:
            shuffled_var1[shuffled_index] = var1[i]
            shuffled_var2[shuffled_index] = var2[i]
            shuffled_Y[shuffled_index] = Y[i]
            shuffled_index += 1
        #end randomizing data

        train_rows = round(rows_num * self.ratio)
        test_rows = rows_num - train_rows

        train_var1 = np.empty((train_rows, columns_num))
        train_var2 = np.empty((train_rows, columns_num))
        train_Y = np.empty((train_rows, columns_num))

        test_var1 = np.empty((test_rows, columns_num))
        test_var2 = np.empty((test_rows, columns_num))
        test_Y = np.empty((test_rows, columns_num))

        train_var1 = shuffled_var1[0:train_rows]
        train_var2 = shuffled_var2[0:train_rows]
        train_Y = shuffled_Y[0:train_rows]

        test_var1 = shuffled_var1[train_rows:]
        test_var2 = shuffled_var2[train_rows:]
        test_Y = shuffled_Y[train_rows:]


        return ((train_var1, train_var2), train_Y, (test_var1, test_var2), test_Y)
