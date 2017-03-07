import subprocess

from Config.ConfigManager import ConfigManager


class RAPI():

    def __init__(self):
        config = ConfigManager()
        configSection = "RNN"
        self._command = config.get_data(configSection, "RCommand")

    def run_script(self, script_path):
        cmd = [self._command, script_path]
        result = subprocess.check_output(cmd, universal_newlines=True)
        return result
