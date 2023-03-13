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
        self.cursor.execute("SELECT * FROM User WHERE email = '"+self.email+"';")
        accInfo = self.cursor.fetchall()[0]
        return accInfo
    
    # returns false if it no worky
    def signupUser(self):
        self.cursor.execute("SELECT first_name, last_name FROM auth_user WHERE email = '"+self.email+"';")
        accInfo = self.cursor.fetchall()[0]
        name = accInfo[0] + " " + accInfo[1]
        
        self.cursor.execute("SELECT COUNT(1) FROM User WHERE email = '"+self.email+"';")
        result = self.cursor.fetchone()[0]
        if(result == 1):
            return False
        
        # set default xp to 0 and default level to 1 -- null pfp?
        self.cursor.execute("INSERT INTO User(email, `Name`, ProfilePictureURL, XP, AwardProfile) VALUES (\""+self.email+"\", \""+name+"\", NULL, 0, 1);")
        return True
        
        
        
        
        
