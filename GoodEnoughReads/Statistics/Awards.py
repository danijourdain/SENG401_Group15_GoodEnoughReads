import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MaxNLocator
from django.db import models
from django.db import connection, transaction
import datetime


class Awards:
    def __init__ (self, level):
        self.level = level
        self.cursor = connection.cursor()

    def getImage(self):
        self.cursor.execute("SELECT Image FROM Awards WHERE Level = '"+self.level+"' ;")
        return self.cursor.fetchall()[0]
    
    def getReqXP(self):
        self.cursor.execute("SELECT Required_XP FROM Awards WHERE Level = '"+self.level+"' ;")
        return self.cursor.fetchall()[0]

    