from os import path

from DTOs.GameData import GameData
from DTOs.RoundData import RoundData


class CsvDAL():

    def read_csv_files(self, folder, file_names):
        dict_list = self._csv_files_to_dict_list(folder, file_names)
        users = self._get_users(dict_list)
        users_dict = {}
        for user in users:
            user_data = self._get_user_data(dict_list, user)
            users_dict[user] = self._build_game_data(user_data)
        return users_dict

    def _build_game_data(self, user_data) -> GameData:
        sorted_data = sorted(user_data, key=lambda x: x["RoundNum"])
        game_data_list = []
        for d in sorted_data:
            game_data_list.append(self._build_round_data(d))
        game_data = GameData()
        game_data.set_rounds_data(game_data_list)
        return game_data

    def _build_round_data(self, d):
        round_data = RoundData()
        round_data.set_AR(d["AR"])
        round_data.set_RoundNum(d["RoundNum"])
        round_data.set_Gain(d["earnPercent"] / 100.0)
        round_data.set_Money(d["money"])
        round_data.set_CommissionMoney(d["commissionMoney"])
        return round_data

    def _get_users(self, data_dict_list):
        return list(set([d['UserId'] for d in data_dict_list]))

    def _get_user_data(self, data_dict_list, userid):
        return [d for d in data_dict_list if d['UserId'] == userid]

    def _csv_files_to_dict_list(self, folder, files_names):
        all_list_data = []
        for file_name in files_names:
            list_data = self._csv_to_dict_list(path.join(folder, file_name) + '.csv')
            all_list_data.extend(list_data)
        return self._build_data_dict_list(all_list_data)

    def _csv_to_dict_list(self, file_name):
        with open(file_name, 'r') as f:
            lines = f.readlines()
        return [[word.replace('\n', '') for word in l.split(',')] for l in lines]

    def _build_data_dict_list(self, list_data):
        data_dict_list = []
        for row in list_data:
            row_dict = {
                'UserId': row[0],
                'RoundNum': int(row[1]),
                'ScenarioNum': int(row[2]),
                'StockId': int(row[3]),
                'money': float(row[4]),
                'moneyInvested': float(row[5]),
                'AR': float(row[5]) / float(row[4]),
                'earnPercent': float(row[6]),
                'earnMoney': float(row[7]),
                'comissionPercent': float(row[8]),
                'commissionMoney': float(row[9]),
                'moneyGettedBack': float(row[10]),
                'endMoney': float(row[11]),
                'isGain': True if row[12] == '1' else False,
                'dateTime': row[14],
                'experimentId': row[15]
            }
            data_dict_list.append(row_dict)
        return data_dict_list



