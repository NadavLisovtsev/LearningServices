from Learning.CrossValidators.DefaultCrossValidator import DefaultCrossValidator
from Learning.CrossValidators.RNNCrossValidator import RNNCrossValidator


class CrossValidatorsFactory():
    def __init__(self):
        self._dict = {
            'RNN': RNNCrossValidator(),
            "Default": DefaultCrossValidator()
        }

    def get_cross_validator(self, name=''):
        return self._dict[name] if name in self._dict.keys() else self._dict["Default"]
