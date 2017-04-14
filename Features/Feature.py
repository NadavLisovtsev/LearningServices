from DTOs.FeatureParams import FeatureParams
from DTOs.GameData import GameData
from DTOs.RawGameData import RawGameData
from DTOs.RawPredictData import RawPredictData
from DTOs.RoundData import RoundData


class Feature:

    def get_raw_data_from_game(self, game_data: GameData, params: FeatureParams) -> RawGameData:
        return self._build_raw_data_from_game_data(game_data, params)

    def get_predict_data(self, game_data: GameData, params: FeatureParams) -> RawPredictData:
        return self._build_predict_data(game_data, params)

    def get_params_values(self):
        return self._get_params_ranges_dict()

    def get_name(self):
        return "Feature"

    def _build_raw_data_from_game_data(self, game_data: GameData, params: FeatureParams) -> RawGameData:
        raise Exception("Not Implemented!! Feature class has no Implementation to this method")

    def _build_predict_data(self, game_data: GameData, params: FeatureParams) -> RawPredictData:
        raise Exception("Not Implemented!! Feature class has no Implementation to this method")

    def _get_params_ranges_dict(self):
        raise Exception("Not Implemented!! Feature class has no Implementation to this method")
