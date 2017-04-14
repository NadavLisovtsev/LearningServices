from DTOs.GameData import GameData
from DTOs.RawGameData import RawGameData
from DTOs.RawPredictData import RawPredictData
from DTOs.RoundData import RoundData
from Features.Feature import Feature


class RoundNumFeature(Feature):

    def _build_raw_data_from_game_data(self, game_data: GameData, params=None) -> RawGameData:
        raw_data = RawGameData()
        for round_num in game_data.get_rounds():
            round_data = game_data.get_round_data(round_num)
            raw_data.add_data_list(self._build_data_from_round(round_data), round_num, self.get_name())
        return raw_data

    def _build_predict_data(self, game_data: GameData, params=None) -> RawPredictData:
        predict_data = RawPredictData()
        predict_data.add_data([game_data.get_last_round().get_RoundNum()])
        return predict_data

    def _build_data_from_round(self, data: RoundData):
        return [data.get_RoundNum()]

    def _get_params_ranges_dict(self):
        return None

    def get_name(self):
        return "RoundNum"
