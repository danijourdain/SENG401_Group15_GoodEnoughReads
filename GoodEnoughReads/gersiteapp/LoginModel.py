import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from django.db import models
from django.db import connection, transaction
import datetime

class LoginModel:
    # initialize loginmodel with the given user
    def __init__(self, email):
        # email is a primary key
        self.email = email
        self.cursor = connection.cursor()

    def retrieveAccountInfo(self):
        self.cursor.execute("SELECT * FROM User WHERE email = %s;", [self.email])
        accInfo = self.cursor.fetchall()[0]
        return accInfo
    
    # returns false if the user already exists
    def verifyUser(self):
        # sql query to check if there is a uer with the same email
        self.cursor.execute("SELECT COUNT(1) FROM User WHERE email = %s;", [self.email])
        result = self.cursor.fetchone()[0]
        if(result == 1):
            # if there exists a user with that email already
            return False
        # otherwise
        return True        
    
    # new user is created, defaults are set, tuples in database are prepared
    def signupUser(self):
        self.cursor.execute("SELECT first_name, last_name FROM auth_user WHERE email = %s;", [self.email])
        accInfo = self.cursor.fetchall()[0]
        name = accInfo[0] + " " + accInfo[1]
        
        # set default xp and default level of the new user to 0
        self.cursor.execute("INSERT INTO User(email, `Name`, XP, AwardProfile) VALUES (%s, %s, 0, 0);", [self.email, name])
        # prepare collection tables in the database that correspond to the new user
        self.cursor.execute("INSERT INTO Collection(`Name`, Email) VALUES (\"read\", %s)", [self.email])
        self.cursor.execute("INSERT INTO Collection(`Name`, Email) VALUES (\"toRead\", %s)", [self.email])
        self.cursor.execute("INSERT INTO Collection(`Name`, Email) VALUES (\"currentlyReading\", %s)", [self.email])
        self.cursor.execute("INSERT INTO Collection(`Name`, Email) VALUES (\"DNF\", %s)", [self.email])
        
        # function worked
        return True
        
    # user updates their name
    def updateUser(self, name):
        # sql query to update the name given the email (primary key) of a user
        self.cursor.execute("UPDATE `User` SET `Name`= %s WHERE Email = %s;", [name, self.email])
