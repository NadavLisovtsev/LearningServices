from DTOs.FeatureParams import FeatureParams


class AllFeaturesParams:
    def __init__(self):
        self._params_dict = {}

    def add_params(self, feature_params: FeatureParams):
        self._params_dict[feature_params.get_feature_name()] = feature_params

    def get_feature_params(self, feature_name):
        return self._params_dict[feature_name] if feature_name in self._params_dict.keys() else None

    def get_all_features(self):
        return self._params_dict.keys()

    def get_pure_dict(self):
        return {p: self._params_dict[p].get_pure_dict() for p in self._params_dict.keys()}

    def init_from_pure_dict(self, pure_dict):
        self._params_dict = []
        for feature_name in pure_dict:
            feature_params = FeatureParams
            feature_params.init_from_pure_dict(pure_dict[feature_name])
            self._params_dict[feature_name] = feature_params
