from Config.ConfigManager import ConfigManager
from Features.RoundNumFeature import RoundNumFeature
from Features.MoneyAmountFeature import MoneyAmountFeature
from Features.LossCountFeature import LossCountFeature
from Features.GainsFeature import GainsFeature
from Features.AvgFirstGainFeature import AvgFirstGainFeature
from Features.ARsFeature import ARsFeature
from Features.YFeature import YFeature


class FeaturesManager:
    def __init__(self):
        self._features_module_name = "Features"
        self._name_to_feature_dict = {
            'RoundNum': 'RoundNumFeature.RoundNumFeature',
            'MoneyAmount': 'MoneyAmountFeature.MoneyAmountFeature',
            'LossCount': 'LossCountFeature.LossCountFeature',
            'Gains': 'GainsFeature.GainsFeature',
            'ARs': 'ARsFeature.ARsFeature',
            'AvgFirstGain': 'AvgFirstGainFeature.AvgFirstGainFeature'
        }

    def get_active_features(self):
        config = ConfigManager()
        feature_names = config.get_data("Features", "ActiveFeatures").split(',')
        return [self._create_feature_instance(self._name_to_feature_dict[f]) for f in feature_names]

    def get_y_feature(self):
        return YFeature()

    def _create_feature_instance(self, f_name):
        sub_module_name = f_name.split('.')[0]
        class_name = f_name.split('.')[1]
        module = __import__(self._features_module_name)
        sub_module = getattr(module, sub_module_name)
        class_ = getattr(sub_module, class_name)
        instance = class_()
        return instance
