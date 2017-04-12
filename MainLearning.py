# coding: utf-8
from Config.ConfigManager import ConfigManager
from DAL.CsvDAL import CsvDAL
from DTOs.AllFeaturesParams import AllFeaturesParams
from DTOs.FeatureParams import FeatureParams
from DataManipulations.DataBuilder import DataBuilder
from Learning.CrossValidators.CrossValidator import CrossValidator
from Learning.CrossValidators.DefaultCrossValidator import DefaultCrossValidator
from Learning.Trainers.TrainersManager import TrainerManager
from Output.OutputManager import OutputManager
from RegressionAlgos.MySVM import MySVM
from RegressionAlgos.RNN.MyRNN import MyRNN
from RegressionAlgos.MyRF import RandomForest


"""
**** checking DAL ****
r = DAL()
users = r.getAllUsers()
results = r.getARandEarnPercentForUser(users[0])
print(results)

*** checking AsymptoticAverage ***
a = AsymptoticAverage()
result = a.calcAverage([0.3, 0.12, 0.56])
print(result)        
result = a.addValToAverage(3.4, 10.8)
print(result)
"""

def build_arbitary_params():
    params = AllFeaturesParams()
    ARparams = FeatureParams("ARs")
    GainParams = FeatureParams("Gains")
    FirstGainAverageParams = FeatureParams("AvgFirstGain")

    ARparams.add_param("ARsCount", 10)
    GainParams.add_param("GainsCount", 10)
    FirstGainAverageParams.add_param("FirstGainCount", 5)
    params.add_params(ARparams)
    params.add_params(GainParams)
    params.add_params(FirstGainAverageParams)

    return params


# *** Find Best Params ***
algo = RandomForest()
csv_reader = CsvDAL()
config = ConfigManager()

folder = config.get_data("CsvData", "Folder")
files_names = config.get_data("CsvData", "FileNames").split(',')
users_dict = csv_reader.read_csv_files(folder, files_names)

params = build_arbitary_params()
data_builder = DataBuilder()
(X, Y) = data_builder.build_xy_data(users_dict, params)
ratio = float(config.get_data("Learning", "testTrainRatio"))


cross_validator = DefaultCrossValidator()
cross_validator.init(X, Y, ratio)
errors = cross_validator.run_algo(algo)

print("")
print(errors.get_errors_list())
print(errors.get_mean_error())



"""
trainer_manager = TrainerManager()
runner = trainer_manager.get_trainer_runner(algos)

trainers_results = runner.run_all_trainers()
results = trainers_results["RNNTrainer"]


output_manager = OutputManager()
printer = output_manager.get_printer("RNN")
printer.print_results(results, algos)
"""

"""
d = {
    'SVM':
        {'ARLookBack': 11,
         'GainLookBack': 7,
         'useARAsymAverage': False,
         'useGainAsymAverage': True,
         'Error': 0.121807882218
         },
    'NN':
        {'ARLookBack': 5,
         'GainLookBack': 9,
         'useARAsymAverage': False,
         'useGainAsymAverage': True,
         'Error': 0.12181901831
         }
    }
print(json.dumps(d))
"""

#run_regression_server(result_directory, best_params_file)





