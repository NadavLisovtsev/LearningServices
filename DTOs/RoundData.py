import json


class RoundData:
    def __init__(self):
        self._data_dict = {}

# <editor-fold desc="Initiators">
    def init_from_json(self, json_data):
        self._data_dict = json.loads(json_data)

    def init_from_dict(self, dict):
        self._data_dict = dict
# </editor-fold>

# <editor-fold desc="Collective Getters">
    def get_json(self):
        return json.dumps(self._data_dict)

    def get_dict(self):
        return self._data_dict
    # </editor-fold>
# </editor-fold>

# <editor-fold desc="Specific Getters">
    def get_AR(self):
        return self._data_dict["AR"]

    def get_Gain(self):
        return self._data_dict["Gain"]

    def get_RoundNum(self):
        return self._data_dict["RoundNum"]

    def get_Money(self):
        return self._data_dict["Money"]

    def get_CommissionMoney(self):
        return self._data_dict["CommissionMoney"]

    def get_InvestedMoney(self):
        return self._data_dict["AR"] * self._data_dict["Money"]

    def get_MoneyGettedBack(self):
        return self.get_InvestedMoney() * (1 + self.get_Gain()) - self.get_CommissionMoney()

    def get_EndMoney(self):
        return self.get_Money() - self.get_InvestedMoney() + self.get_MoneyGettedBack()
# </editor-fold>

# <editor-fold desc="Setters">
    def set_AR(self, AR):
        self._data_dict["AR"] = AR

    def set_Gain(self, Gain):
        self._data_dict["Gain"] = Gain

    def set_RoundNum(self, RoundNum):
        self._data_dict["RoundNum"] = RoundNum

    def set_Money(self, Money):
        self._data_dict["Money"] = Money

    def set_CommissionMoney(self, CommissionMoney):
        self._data_dict["CommissionMoney"] = CommissionMoney

# </editor-fold>

