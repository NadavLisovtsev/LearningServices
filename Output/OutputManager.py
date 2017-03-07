import json

import numpy as np

from Output.Printers.DefaultPrinter import DefaultPrinter
from Output.Printers.RNNPrinter import RNNPrinter


class OutputManager:

    def __init__(self):
        self.printers_dict = {
            'RNN': RNNPrinter(),
            'Default': DefaultPrinter()
        }

    def get_printer(self, algo_name):
        return self.printers_dict[algo_name] if algo_name in self.printers_dict.keys() \
            else self.printers_dict["Default"]

