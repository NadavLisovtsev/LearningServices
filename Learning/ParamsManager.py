import json

from Config.ConfigManager import ConfigManager
from DTOs.AllFeaturesParams import AllFeaturesParams


class ParamsManager:
    def __init__(self):
        config = ConfigManager()
        self._params_file = config.get_data("ParamsManager", "ParamsFile")
        self._algo_params_dict = None

    def get_params_for_algo(self, algo_name) -> AllFeaturesParams:
        if self._algo_params_dict is None:
            self._init_params_dict()
        return self._algo_params_dict[algo_name]

    def add_params_for_algo(self, algo_name, features_params: AllFeaturesParams):
        self._algo_params_dict[algo_name] = features_params

    def save_params(self):
        pure_dict = {algo_name: self._algo_params_dict[algo_name].get_pure_dict() for algo_name in self._algo_params_dict.keys()}
        with open(self._params_file, 'w') as f:
            f.write(json.dumps(pure_dict))

    def _init_params_dict(self):
        self._algo_params_dict = {}
        with open(self._params_file, 'r') as f:
            pure_dict = json.loads(f.read())
        for algo_name in pure_dict.keys():
            features_params = AllFeaturesParams()
            features_params.init_from_pure_dict(pure_dict[algo_name])
            self._algo_params_dict[algo_name] = features_params
