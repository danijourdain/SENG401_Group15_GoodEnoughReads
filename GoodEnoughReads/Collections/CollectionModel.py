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
        self.cursor.execute("INSERT INTO BookInUserCollection VALUES (%s, %s, %s, %s, %s);", [startdate, enddate, pagesread, isbn, email])
        
    def getName(self):
        self.cursor.execute("SELECT Name FROM Collection WHERE Email = %s;", [self.email])
        return self.cursor.fetchall()[0]
    
    def getBooksInCollection(self, shelfName):
        self.cursor.execute("SELECT ISBN FROM BookInUserCollection WHERE Email = %s;", [self.email])
        bookList = self.cursor.fetchall()
        return bookList
    
    # user passes in a book, gets every collection of theirs with said book
    def collectionsWithBook(self, bookisbn):
        self.cursor.execute("SELECT ShelfName FROM BookInUserCollection WHERE Email = %s AND ISBN = %s;", [self.email, bookisbn])
        cols = self.cursor.fetchall()
        return cols