class FeatureParamsBuilder():
    def __init__(self):
        self._params_dict = {}

    def set_params(self, f_name, params):
        self._params_dict[f_name] = params

    def get_params(self, f_name):
        if f_name not in self._params_dict.keys():
            return None
        return self._params_dict[f_name]
