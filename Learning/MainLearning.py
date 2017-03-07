# coding: utf-8

from Learning.Trainers.TrainersManager import TrainerManager
from Output.OutputManager import OutputManager
from RegressionAlgos.RNN.MyRNN import MyRNN

print('Yay :)')

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


# *** Find Best Params ***
algos = [MyRNN()]

trainer_manager = TrainerManager()
runner = trainer_manager.get_trainer_runner(algos)

trainers_results = runner.run_all_trainers()
results = trainers_results["RNNTrainer"]


output_manager = OutputManager()
printer = output_manager.get_printer("RNN")
printer.print_results(results, algos)


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





