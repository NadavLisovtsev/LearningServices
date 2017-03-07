from Config.ConfigParser import ConfigParser
from Singleton import Singleton


class ConfigManager(metaclass=Singleton):
    def __init__(self):

        self._env_file = r"Config/config.ini"
        self._files_dict = {
            'Dev': r"Config/dev.ini",
            'Prod': r"Config/prod.ini"
        }

        parser = ConfigParser()
        parser.read_file(self._env_file)
        self._env = parser.options("Enviorment")["currEnv"]

        self._config = self._create_config_from_file()

    def _create_config_from_file(self):
        config_file = self._files_dict[self._env]
        parser = ConfigParser()
        parser.read_file(config_file)

        config_dict = {}
        for section in parser.sections():
            config_dict[section] = parser.options(section)

        return config_dict

    def get_data(self, section, option):
        return self._config[section][option]
