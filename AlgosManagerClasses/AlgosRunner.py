from DataManipulations.DataOrganizersFactory import DataOrganizerFactory


class AlgosRunner:

    def run_algo(self, algo, ars, gains, params=None):
        algo_name = algo.get_name()

        organizer_factory = DataOrganizerFactory()
        data_organizer = organizer_factory.get_organizer(algo_name)
        data = data_organizer.organize_prediction_data(ars, gains, params)

        result = algo.get_prediction(data)
        return result
