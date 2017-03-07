from DataManipulations.AverageAlgorithm.AVGDataOrganizer import AVGDataOrganizer
from DataManipulations.DataOrganizer import DataOrganizer
from DataManipulations.LinearRegression.LRDataOrganizer import LRDataOrganizer
from DataManipulations.RNN.RNNDataOrganizer import RNNDataOrganizer


class DataOrganizerFactory():
    def __init__(self):
        self._builder_dict = {
            'RNN': RNNDataOrganizer(),
            'AVG': AVGDataOrganizer(),
            'LR': LRDataOrganizer(),
            'Default': DataOrganizer()
        }

    def get_organizer(self, name):
        return self._builder_dict[name] if name in self._builder_dict.keys() else self._builder_dict['Default']
