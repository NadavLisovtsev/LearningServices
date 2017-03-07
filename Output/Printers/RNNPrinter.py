import csv

from Config.ConfigManager import ConfigManager


class RNNPrinter():
    def __init__(self):
        config = ConfigManager()
        self.output_directory = config.get_data("RNN", "train_data_directory")
        self.results_file = config.get_data("RNN", "results_file")

    def save_train_data(self, variables_matrix, Y):
        self.__save_variables_matrix(variables_matrix, self.output_directory, "var")
        filename = "Y.csv"
        self.__save_varaibale_to_csv(Y, self.output_directory + filename)

    def save_test_data(self, variables_matrix, Y):
        self.__save_variables_matrix(variables_matrix, self.output_directory, "testX")
        self.__save_varaibale_to_csv(Y, self.output_directory + "testY.csv")

    def save_prediction_data(self, variables_matrix):
        base_filename = "predict"
        count = 1
        for var in variables_matrix:
            filename = base_filename + str(count) + ".csv"
            self.__save_one_row_variable(var, self.output_directory + filename)
            count += 1

    def __save_variables_matrix(self, variables_matrix, directory, base_filename):
        count = 1
        for var in variables_matrix:
            filename = base_filename + str(count) + ".csv"
            self.__save_varaibale_to_csv(var, directory + filename)
            count += 1

    def __save_varaibale_to_csv(self, variable, filename):
            with open(filename, 'w') as f:
                writer = csv.writer(f, delimiter=',')
                for row in variable:
                    writer.writerow(row)


    def __save_one_row_variable(self, variable, filename):
        with open(filename, 'w') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(variable)


    def print_results(self, results, algos):
        with open(self.results_file, 'w') as f:
            f.write(str(results[0]))

