from AlgosManagerClasses.AlgosManager import AlgosManager


class MinRoundsHandler:

    def handle_request(self, json_data):

        manager = AlgosManager()
        name = json_data["Name"]
        return manager.get_algo_look_back(name)