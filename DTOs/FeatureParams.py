class FeatureParams:
    def __init__(self, feature_name):
        self._feature_name = feature_name
        self._params_dict = {}
        self._look_back = 0

    def add_param(self, name, value, is_look_back=False):
        self._params_dict[name] = value
        if is_look_back:
            self._look_back = value + 1

    def get_param(self, name):
        return self._params_dict[name]

    def get_all_params_names(self):
        return self._params_dict.keys()

    def get_feature_name(self):
        return self._feature_name

    def get_pure_dict(self):
        return {
            'feature_name': self._feature_name,
            'params_dict': self._params_dict
        }

    def init_from_pure_dict(self, pure_dict):
        self._params_dict = pure_dict["params_dict"]
        self._feature_name = pure_dict["feature_name"]

    def get_look_back(self):
        return self._look_back

