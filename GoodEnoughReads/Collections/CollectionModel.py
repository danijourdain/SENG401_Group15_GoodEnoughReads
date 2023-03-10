import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from django.db import models
from django.db import connection, transaction
import datetime

class CollectionModel:
    def __init__(self, email):
        self.email = email
        self.cursor = connection.cursor()

    def addToCollection(self, email, isbn, startdate, enddate, pagesread):
        # more functionality?
        self.cursor.execute("INSERT INTO BookInUserCollection "+startdate+", "+enddate+", "+pagesread+", "+isbn+", "+email+"")
        
    def getName(self):
        self.cursor.execute("SELECT Name FROM Collection WHERE Email = '" + self.email + "' ;")
        return self.cursor.fetchall()[0]