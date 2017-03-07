from AlgosManagerClasses.AlgosManager import AlgosManager
from PredictionServerClasses.APIHandler import APIHandler


def run_regression_server():

    print('Starting...')
    manager = AlgosManager()

    manager.init_algos()
    manager.train_algos()

    print('manager initialized')

    # starting server
    api = APIHandler()
    api.start_server(1234)


run_regression_server()
