from DTOs.GameData import GameData
from DTOs.RawGameData import RawGameData
from DTOs.RawPredictData import RawPredictData
from DTOs.RoundData import RoundData
from Features.Feature import Feature


class LossCountFeature(Feature):

    def _build_raw_data_from_game_data(self, game_data: GameData, params=None) -> RawGameData:
        raw_data = RawGameData()
        data_dict = game_data.get_rounds_data_dict()
        loss_count = 0
        index = 0
        for round_num in data_dict.keys():
            round_data = data_dict[round_num]
            if index > 0:
                raw_data.add_data_list([loss_count], round_num, self.get_name())
            loss_count += 1 if round_data.get_Gain() < 0 else 0
            index += 1
        return raw_data

    def _build_predict_data(self, game_data: GameData, params=None) -> RawPredictData:
        predict_data = RawPredictData()
        loss_count = 0
        for round_num in game_data.get_prev_rounds():
            round_data = game_data.get_round_data(round_num)
            loss_count += 1 if round_data.get_Gain() < 0 else 0
        predict_data.add_data([loss_count])
        return predict_data

    def _get_params_ranges_dict(self):
        return None

    def get_name(self):
        return "LossCount"