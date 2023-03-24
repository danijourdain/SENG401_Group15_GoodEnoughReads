# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
# from matplotlib.ticker import MaxNLocator
from django.db import models
from django.db import connection, transaction
# import datetime


class Awards:
    def __init__ (self, email):
        self.email = email
        self.cursor = connection.cursor()

    # def getImage(self, level):
    #     self.cursor.execute("SELECT Image FROM Awards WHERE Level = ?;", level)
    #     return self.cursor.fetchall()[0]
    
    def getReqXP(self, level):
        level = str(level)
        self.cursor.execute("SELECT Required_XP FROM Awards WHERE Level = %s;", [level])
        return self.cursor.fetchall()[0][0]
    
    def getUserXP(self):
        self.cursor.execute("SELECT XP FROM User WHERE Email = %s;", [self.email])
        return self.cursor.fetchall()[0][0]

    def getUserLevel(self):
        self.cursor.execute("SELECT AwardProfile FROM User WHERE Email = %s;", [self.email])
        self.UserLevel = self.cursor.fetchall()[0][0]
        return self.UserLevel
    
    def updateUserLevel(self):
        self.cursor.execute("UPDATE User SET AwardProfile = %s WHERE Email = %s;", [self.UserLevel + 1, self.email])
        # self.cursor.execute("SELECT AwardProfile FROM User WHERE Email = %s;", [self.email])
        # return self.cursor.fetchall()[0][0]
        
    def updateUserXP(self, xp):
        self.cursor.execute("UPDATE User SET XP = %s WHERE Email = %s;", [xp, self.email])


    