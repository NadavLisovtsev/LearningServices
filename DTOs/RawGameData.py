import numpy as np
import types


class RawGameData:
    def __init__(self):
        self._rounds_dict = {}
        self._features_names_dict = {}
        self._features = set()

    def add_data_list(self, data_list, round_num, features_names):
        if not type(features_names) is list:
            features_names = [features_names]

        self._features = self._features | set(features_names)  # union two sets
        if round_num not in self._features_names_dict.keys():
            self._features_names_dict[round_num] = features_names
        else:
            self._features_names_dict[round_num].extend(features_names)

        if round_num not in self._rounds_dict.keys():
            self._rounds_dict[round_num] = [data_list, None]
        else:
            self._rounds_dict[round_num][0].extend(data_list)

    def set_y(self, round_num, y):
        if round_num not in self._rounds_dict.keys():
            self._rounds_dict[round_num] = [[], y]
        else:
            self._rounds_dict[round_num][1] = y

    def get_y(self, round_num):
        if round_num not in self._rounds_dict.keys():
            return None
        else:
            return self._rounds_dict[round_num][1]

    def get_data_list(self, round_num):
        if round_num not in self._rounds_dict.keys():
            return []
        else:
            return self._rounds_dict[round_num][0]

    def get_existed_rounds(self):
        return self._rounds_dict.keys()

    def get_features_for_round(self, round_num):
        if round_num not in self._features_names_dict.keys():
            return []
        else:
            return self._features_names_dict[round_num]

    def get_all_features(self):
        return list(self._features)

    def delete_round_data(self, round_num):
        self._rounds_dict.pop(round_num, None)

    def merge_raw_game_data(self, raw_game_data):
        for round in raw_game_data.get_existed_rounds():
            data_list = raw_game_data.get_data_list(round)
            y = raw_game_data.get_y(round)
            features = raw_game_data.get_features_for_round(round)
            self.add_data_list(data_list, round, features)
            if self._rounds_dict[round][1] is None:
                self.set_y(round, y)

    def get_XY_matrix(self):
        relevant_rounds = [r for r in self._features_names_dict.keys()
                           if set(self._features_names_dict[r]) == self._features
                           and self._rounds_dict[r][1] is not None]
        rows = len(relevant_rounds)
        columns = len(self._rounds_dict[relevant_rounds[0]][0])
        X = np.empty((rows, columns), 'float64')
        Y = np.empty(rows, 'float64')
        i = 0
        for round in relevant_rounds:
            Y[i] = self._rounds_dict[round][1]
            X[i] = np.asarray(self._rounds_dict[round][0])
            i += 1

        return X, Y
    



