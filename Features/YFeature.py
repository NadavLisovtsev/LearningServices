from DTOs.GameData import GameData
from DTOs.RawGameData import RawGameData
from DTOs.RoundData import RoundData
from Features.Feature import Feature


class YFeature(Feature):
    def _build_raw_data_from_game_data(self, game_data: GameData, params=None) -> RawGameData:
        raw_data = RawGameData()
        for round_num in game_data.get_rounds():
            round_data = game_data.get_round_data(round_num)
            raw_data.set_y(round_num, round_data.get_AR())
        return raw_data

    def _get_params_ranges_dict(self):
        return None

    def get_name(self):
        return "Y"
