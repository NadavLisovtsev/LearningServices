from AlgosManagerClasses.AlgosManager import AlgosManager


class RegressionHandler:

     def handle_request(self, json_data):
        algo_name = json_data['Name']

        manager = AlgosManager()
        raw_data = json_data['RawData']
        result = manager.run_algo(algo_name, raw_data['AR'], raw_data['Gain'])
        return result