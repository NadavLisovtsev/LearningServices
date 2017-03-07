from PredictionServerClasses.RequestsHandlers.MinRoundsHandler import MinRoundsHandler
from PredictionServerClasses.RequestsHandlers.RegressionHandler import RegressionHandler


class RequestsRouter:
    def __init__(self):
        self.handlers = {
            'Regression': RegressionHandler(),
            'MinRounds': MinRoundsHandler()
        }

    def get_handler(self, method):
        return self.handlers[method]