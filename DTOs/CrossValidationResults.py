import numpy as np

class CrossValidationResults:
    def __init__(self):
        self._errors = []

    def add_error(self, error):
        self._errors.append(error)

    def get_num_errors(self):
        return len(self._errors)

    def get_mean_error(self):
        return np.mean(self._errors)

    def get_errors_func_result(self, func):
        return func(self._errors)

    def get_errors_list(self):
        return self._errors

