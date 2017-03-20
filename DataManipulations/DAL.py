import sys
import sqlite3 as lite

from Config.ConfigManager import ConfigManager


class DAL:
    def readData(self, query):
        con = None
        config = ConfigManager()


        try:
            db_file = config.get_data("DAL", "DBFile")
            con = lite.connect(db_file)
            cur = con.cursor()
            cur.execute(query)
            row = []
            data = []
            while (row != None):
                row = cur.fetchone()
                data.append(row)

            return data

        except Exception as e:

            print("Error %s:" % e.args[0])
            con.close()
            sys.exit(1)
        finally:
            con.close()


    def getAllUsers(self):
        query  = "select UserId from UserInvestments where UserId != 'friend' group by UserId"
        data =self.readData(query)
        users = []
        for i in data:
            users.append(str(i)[2:-3])
        return users

    def getARandEarnPercentForUser(self, user):
        query = "select moneyInvested / money, earnPercent / 100.0 from UserInvestments where UserId = '" + user + "' and isTraining = 0 order by RoundNum asc"
        data = self.readData(query)
        ARandEarn = []
        for i in data:
            if i != None:
                ARandEarn.append(i)
        return ARandEarn

