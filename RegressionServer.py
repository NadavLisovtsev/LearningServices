from AlgosManagerClasses.AlgosManager import AlgosManager
from AlgosManagerClasses.NewAlgosManager import NewAlgosManager
from Config.ConfigManager import ConfigManager
from DAL.CsvDAL import CsvDAL
from Learning.ParamsManager import ParamsManager
from PredictionServerClasses.APIHandler import APIHandler


def run_regression_server():

    print('Starting...')
    manager = NewAlgosManager()

    manager.init_algos()

    csv_reader = CsvDAL()
    config = ConfigManager()

    folder = config.get_data("CsvData", "Folder")
    files_names = config.get_data("CsvData", "FileNames").split(',')
    users_dict = csv_reader.read_csv_files(folder, files_names)

    manager.train_algos(users_dict)

    print('manager initialized')

    # starting server
    api = APIHandler()
    api.start_server(1234)


run_regression_server()
