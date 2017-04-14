from AlgosManagerClasses.AlgosManager import AlgosManager


from Learning.ParamsManager import ParamsManager


class MinRoundsHandler:

    def handle_request(self, json_data):

        params_manager = ParamsManager()
        name = json_data["Name"]
        return params_manager.get_algo_look_back(name)