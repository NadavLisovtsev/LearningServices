from DataManipulations.AverageAlgorithm.AVGDataBuilder import AVGDataBuilder
from DataManipulations.DataBuilder import DataBuilder
from DataManipulations.LinearRegression.LRDataBuilder import LRDataBuilder
from DataManipulations.RNN.RNNDataBuilder import RNNDataBuilder


class DataBuilderFactory:
    def __init__(self):
        self._builder_dict = {
            'RNN': self.__RNN_creator,
            'LR': self.__LR_creator,
            'AVG': self.__AVG_creator,
            'Default': self.__Deafult_creator
        }

    def get_builder(self, name):
        creation_func =  self._builder_dict[name] if name in self._builder_dict.keys() else self._builder_dict['Default']
        return creation_func()
     #   class_name = class_attributes[0]
     #   class_module = class_attributes[1]
     #   return self.__create_instance(class_name, class_module)

    # Freations Functions

    def __RNN_creator(self):
        return RNNDataBuilder()

    def __AVG_creator(self):
        return AVGDataBuilder()

    def __LR_creator(self):
        return LRDataBuilder()

    def __Deafult_creator(self):
        return DataBuilder()


    # END of creations functions


    def __create_instance(self, class_name, module_name):
        modules_list = module_name.split('.')
        module = __import__(modules_list[0])
        for i in range(1, len(modules_list)):
            module = getattr(module, modules_list[i])
        class_ = getattr(module, class_name)
        return class_()
