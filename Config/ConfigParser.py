
class ConfigParser:
    def __init__(self):
        self._options_dict = {}

    def read_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            last_env = ""
            for l in lines:
                if l[0] == '[':
                    l = self.__no_spaces(l)
                    env_name = l[1:-1]
                    self._options_dict[env_name] = {}
                    last_env = env_name
                elif len(self.__no_spaces(l)) != 0:
                    splitted = l.split()
                    key = splitted[0][:-1]
                    value = splitted[1]
                    self._options_dict[last_env][key] = value
                else:
                    continue
        return self._options_dict

    def options(self, env):
        return self._options_dict[env]

    def sections(self):
        return self._options_dict.keys()

    def __no_spaces(self, s):
        return "".join(s.split())