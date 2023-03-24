import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from django.db import models
from django.db import connection, transaction
import datetime

class LoginModel:
    def __init__(self, email):
        self.email = email
        self.cursor = connection.cursor()

    def retrieveAccountInfo(self):
        self.cursor.execute("SELECT * FROM User WHERE email = %s;", [self.email])
        accInfo = self.cursor.fetchall()[0]
        return accInfo
    
    # returns false if the user already exists
    def verifyUser(self):
        self.cursor.execute("SELECT COUNT(1) FROM User WHERE email = %s;", [self.email])
        result = self.cursor.fetchone()[0]
        if(result == 1):
            return False
        
        return True        
    
    def signupUser(self):
        self.cursor.execute("SELECT first_name, last_name FROM auth_user WHERE email = %s;", [self.email])
        accInfo = self.cursor.fetchall()[0]
        name = accInfo[0] + " " + accInfo[1]
        
        # set default xp to 0 and default level to 1 -- null pfp%s
        self.cursor.execute("INSERT INTO User(email, `Name`, XP, AwardProfile) VALUES (%s, %s, 0, 0);", [self.email, name])
        self.cursor.execute("INSERT INTO Collection(`Name`, Email) VALUES (\"read\", %s)", [self.email])
        self.cursor.execute("INSERT INTO Collection(`Name`, Email) VALUES (\"toRead\", %s)", [self.email])
        self.cursor.execute("INSERT INTO Collection(`Name`, Email) VALUES (\"currentlyReading\", %s)", [self.email])
        self.cursor.execute("INSERT INTO Collection(`Name`, Email) VALUES (\"DNF\", %s)", [self.email])
        return True
        
    def updateUser(self, name):
        self.cursor.execute("UPDATE `User` SET `Name`= %s WHERE Email = %s;", [name, self.email])
