from DTOs import RoundData


class GameData:
    def __init__(self):
        self._rounds_dict = {}

    def set_rounds_data(self, rounds_data, start_round=1):
        i = start_round
        for data in rounds_data:
            self._rounds_dict[i] = data
            i += 1

    def add_round_data(self, data: RoundData, round_num):
        self._rounds_dict[round_num] = data

    def get_round_data(self, round_num):
        return self._rounds_dict[round_num]

    def get_rounds_data_dict(self):
        return self._rounds_dict

    def get_rounds(self):
        return self._rounds_dict.keys()

    def get_prev_rounds_dict(self, round_num):
        return {r: self._rounds_dict[r] for r in self._rounds_dict.keys() if r < round_num}

    def get_last_round(self):
        last_round = list(self._rounds_dict.keys())[-1]
        return self._rounds_dict[last_round]

