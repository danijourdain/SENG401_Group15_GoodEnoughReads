from django.db import models
from django.db import connection, transaction


class Awards:
    def __init__ (self, email):
        self.email = email
        self.cursor = connection.cursor()

    def getReqXP(self, level):
        # get XP to reach level
        level = str(level)
        self.cursor.execute("SELECT Required_XP FROM Awards WHERE Level = %s;", [level])
        return self.cursor.fetchall()[0][0]
    
    def getUserXP(self):
        # get XP user currently has
        self.cursor.execute("SELECT XP FROM User WHERE Email = %s;", [self.email])
        return self.cursor.fetchall()[0][0]

    def getUserLevel(self):
        # get current user level
        self.cursor.execute("SELECT AwardProfile FROM User WHERE Email = %s;", [self.email])
        self.UserLevel = self.cursor.fetchall()[0][0]
        return self.UserLevel
    
    def updateUserLevel(self):
        # update user level with 1 + self.userlevel
        self.cursor.execute("UPDATE User SET AwardProfile = %s WHERE Email = %s;", [self.UserLevel + 1, self.email])
        
    def updateUserXP(self, xp):
        # update user XP to xp
        self.cursor.execute("UPDATE User SET XP = %s WHERE Email = %s;", [xp, self.email])


    