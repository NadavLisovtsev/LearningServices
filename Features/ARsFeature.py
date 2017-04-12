from Config.ConfigManager import ConfigManager
from DTOs.FeatureParams import FeatureParams
from DTOs.GameData import GameData
from DTOs.RawGameData import RawGameData
from DTOs.RoundData import RoundData
from Features.Feature import Feature


class ARsFeature(Feature):

    def _build_raw_data_from_game_data(self, game_data: GameData, params: FeatureParams) -> RawGameData:
        raw_data = RawGameData()
        data_dict = game_data.get_rounds_data_dict()
        ARs_list = []
        count = params.get_param("ARsCount")
        index = 0
        for round_num in data_dict.keys():
            round_data = data_dict[round_num]
            if index >= count:
                raw_data.add_data_list(ARs_list[-count:], round_num, self.get_name())
            ARs_list.append(round_data.get_AR())
            index += 1
        return raw_data

    def _get_params_ranges_dict(self):
        config = ConfigManager()
        rng = config.get_data("Features", "ARRange").split(',')
        return range(rng[0]+1, rng[1]+1)

    def get_name(self):
        return "ARs"