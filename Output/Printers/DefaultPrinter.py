import json

from Config.ConfigManager import ConfigManager


class DefaultPrinter():

    def __init__(self):
        config = ConfigManager()
        config_section = "DefaultPrinter"
        self.result_directory = config.get_data(config_section, "result_directory")
        self.best_options_file = config.get_data(config_section, "best_options_file")
        self.best_options_json = config.get_data(config_section, "best_options_json")

    def print_results(self, results, algos):
        self.printResults(results, algos, self.result_directory)
        self.printBestsPerOption(algos, results, self.best_options_file)
        self.printBestsForAll(algos, results, self.best_options_json)


    def printOptionToFile(self, option, optionName, algos, outputDirectory):

        errors = option['Errors']
        algos_num = len(algos)

        for i in range(algos_num):
            filename = algos[i].get_name() + "Errors" + optionName + ".txt"
            f = open(outputDirectory + filename, 'w')
            f.close()
            np.savetxt(outputDirectory + filename, errors[0])

    def printResults(self, results, algos, outputDirectory):
        self.printOptionToFile(results["NoAsym"], "NoAsym", algos, outputDirectory)
     #   self.printOptionToFile(results["OnlyARAsym"], "OnlyARAsym", algos, outputDirectory)
     #   self.printOptionToFile(results["OnlyGainAsym"], "OnlyGainAsym", algos, outputDirectory)
     #   self.printOptionToFile(results["BothAsym"], "BothAsym", algos, outputDirectory)

    def printBestsPerOption(self, algos, results, output_file):
        output = ""
        i = 0
        for algo in algos:
            output = output + algo.get_name() + ":" + '\n'
            for option in results:
                best = results[option]['Best'][i]
                output = output + option +  " Best: " + str(best[0]) + " AR lookBack: " + str(best[1]) + " Gain lookBack: " + str(best[2])
                output += '\n'
            i += 1

        with open(output_file, 'w') as f:
            f.write(output)

    def printBestsForAll(self, algos, results, output_file):

        bestDict = {}
        i = 0
        for algo in algos:
            bestError = 1.0
            for option in results:
                asymAverageUse = self.extractUseFromOptionName(option)
                bestParams = results[option]['Best'][i]
                if bestParams[0] < bestError:
                    bestError = bestParams[0]
                    bestDict[algo.get_name()] = {
                        'ARLookBack': bestParams[1],
                        'GainLookBack': bestParams[2],
                        'useARAsymAverage': asymAverageUse['AR'],
                        'useGainAsymAverage': asymAverageUse['Gain'],
                        'Error': bestError
                    }
        i += 1
        output = json.dumps(bestDict)
        with open(output_file, 'w') as f:
            f.write(output)

    def extractUseFromOptionName(self, option):
        ar = False
        gain = False
        if option == 'OnlyARAsym':
            ar = True
        elif option == 'OnlyGainAsym':
            gain = True
        elif option == 'BothAsym':
            ar = True
            gain = True

        return {
            'AR': ar,
            'Gain': gain
        }