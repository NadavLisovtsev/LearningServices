import numpy as np


class RawPredictData:
    def __init__(self):
        self._data_list = []

    def add_data(self, data):
        self._data_list.extend(data)

    def get_data_list(self):
        return self._data_list

    def get_X_vector(self):
        return np.asarray(self._data_list)

    def merge_raw_predict_data(self, predict_data):
        self._data_list.extend(predict_data.get_data_list())
