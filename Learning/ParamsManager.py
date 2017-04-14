import json

from Config.ConfigManager import ConfigManager
from DTOs.AllFeaturesParams import AllFeaturesParams
from DTOs.FeatureParams import FeatureParams


class ParamsManager:
    def __init__(self):
        config = ConfigManager()
        self._use_file_init = False
        self._params_file = config.get_data("ParamsManager", "ParamsFile")
        self._algo_params_dict = None

    def get_params_for_algo(self, algo_name) -> AllFeaturesParams:
        if self._algo_params_dict is None:
            if self._use_file_init:
                self._init_params_dict_from_file()
            else:
                self._init_from_default(algo_name)
        return self._algo_params_dict[algo_name]

    def add_params_for_algo(self, algo_name, features_params: AllFeaturesParams):
        self._algo_params_dict[algo_name] = features_params

    def save_params(self):
        pure_dict = {algo_name: self._algo_params_dict[algo_name].get_pure_dict() for algo_name in self._algo_params_dict.keys()}
        with open(self._params_file, 'w') as f:
            f.write(json.dumps(pure_dict))

    def get_algo_look_back(self, algo_name):
        params = self.get_params_for_algo(algo_name)
        return params.get_look_back()

    def _init_from_default(self, algo_name):
        params = AllFeaturesParams()
        ARparams = FeatureParams("ARs")
        GainParams = FeatureParams("Gains")
        FirstGainAverageParams = FeatureParams("AvgFirstGain")

        ARparams.add_param("ARsCount", 5, True)
        GainParams.add_param("GainsCount", 5, True)
        FirstGainAverageParams.add_param("FirstGainCount", 2, True)
        params.add_params(ARparams)
        params.add_params(GainParams)
        params.add_params(FirstGainAverageParams)

        self._algo_params_dict = {}
        self._algo_params_dict[algo_name] = params



    def _init_params_dict_from_file(self):
        self._algo_params_dict = {}
        with open(self._params_file, 'r') as f:
            pure_dict = json.loads(f.read())
        for algo_name in pure_dict.keys():
            features_params = AllFeaturesParams()
            features_params.init_from_pure_dict(pure_dict[algo_name])
            self._algo_params_dict[algo_name] = features_params
