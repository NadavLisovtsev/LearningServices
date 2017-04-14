from AlgosManagerClasses.AlgosManager import AlgosManager
from AlgosManagerClasses.NewAlgosManager import NewAlgosManager
from DTOs.GameData import GameData


class RegressionHandler:

     def handle_request(self, json_data):
        algo_name = json_data['Name']

        manager = NewAlgosManager()
        game_data_list = json_data['GameData']
        game_data = GameData()
        game_data.init_from_pure_list(game_data_list)
        result = manager.run_algo(algo_name, game_data)
        return result