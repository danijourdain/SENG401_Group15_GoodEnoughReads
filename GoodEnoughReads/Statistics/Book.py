import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from django.db import models
from django.db import connection, transaction
import datetime

class Book:
    def __init__(self):
        self.cursor = connection.cursor()

    def getISBN():
        pass
        
    def getTitle():
        pass
    
    def getGenre():
        pass

    def getPages():
        pass

    def getRating():
        pass

    def getType():
        pass

    def getAuthors():
        pass

    def getEndDate():
        # Perform query to find the date the user finishes reading a book
        pass 
