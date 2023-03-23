import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from django.db import models
from django.db import connection, transaction
from django.views import View
from search import BookModel
import datetime


class CollectionModel:
    def __init__(self):
        self.email = None
        self.cursor = connection.cursor()

    def setEmail(self, email):
        self.email = email

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
    
    # Description: Function gets every book in the user's collection regardless of the shelf it is being added to. It then takes this information and 
    # places that data in a temporary book function that the template can access and retrieve without the use of the API. 
    def getAllCollection(self):
        self.cursor.execute("SELECT B.ImageURL, B.Title, B.Pages, BC.UserRating FROM Book AS B INNER JOIN BookInUserCollection as BC ON B.APIid = BC.ISBN AND BC.Email = %s;", [self.email])
        tupleInfo = self.cursor.fetchall()
        list = []
        print(tupleInfo)
        for i in range(len(tupleInfo)): #Non python loop so that specific class variables can be accessed and retrieved since the database is not returning the entire book tuple
            book = BookModel.BookModel()
            book.bookImg = tupleInfo[i][0]
            book.title = tupleInfo[i][1]
            book.pageCount = tupleInfo[i][2]
            book.userRating = tupleInfo[i][3]
            list.append(book)

        return list
    
    # Description: Function gets every book in the user's read collection. It then takes this information and 
    # places that data in a temporary book function that the template can access and retrieve without the use of the API. 
    def getRead(self):
        self.cursor.execute("SELECT B.ImageURL, B.Title, B.Pages, BC.UserRating FROM Book AS B INNER JOIN BookInUserCollection as BC ON B.APIid = BC.ISBN AND BC.shelfName = 'read' AND BC.Email = %s;", [self.email])
        tupleInfo = self.cursor.fetchall()
        list = []
        print(tupleInfo)
        for i in range(len(tupleInfo)):
            book = BookModel.BookModel()
            book.bookImg = tupleInfo[i][0]
            book.title = tupleInfo[i][1]
            book.pageCount = tupleInfo[i][2]
            book.userRating = tupleInfo[i][3]
            list.append(book)

        return list
    
    # Description: Function gets every book in the user's toRead collection. It then takes this information and 
    # places that data in a temporary book function that the template can access and retrieve without the use of the API. 
    def gettoRead(self):
        self.cursor.execute("SELECT B.ImageURL, B.Title, B.Pages, BC.UserRating FROM Book AS B INNER JOIN BookInUserCollection as BC ON B.APIid = BC.ISBN AND BC.shelfName = 'toRead' AND BC.Email = %s;", [self.email])
        tupleInfo = self.cursor.fetchall()
        list = []
        print(tupleInfo)
        for i in range(len(tupleInfo)):
            book = BookModel.BookModel()
            book.bookImg = tupleInfo[i][0]
            book.title = tupleInfo[i][1]
            book.pageCount = tupleInfo[i][2]
            book.userRating = tupleInfo[i][3]
            list.append(book)

        return list
    
    # Description: Function gets every book in the user's currently reading collection. It then takes this information and 
    # places that data in a temporary book function that the template can access and retrieve without the use of the API. 
    def getcurrentlyReading(self):
        self.cursor.execute("SELECT B.ImageURL, B.Title, B.Pages, BC.UserRating FROM Book AS B INNER JOIN BookInUserCollection as BC ON B.APIid = BC.ISBN AND BC.shelfName = 'currentlyReading' AND BC.Email = %s;", [self.email])
        tupleInfo = self.cursor.fetchall()
        list = []
        print(tupleInfo)
        for i in range(len(tupleInfo)):
            book = BookModel.BookModel()
            book.bookImg = tupleInfo[i][0]
            book.title = tupleInfo[i][1]
            book.pageCount = tupleInfo[i][2]
            book.userRating = tupleInfo[i][3]
            list.append(book)

        return list

    # Description: Function gets every book in the user's DNF (did not finish) collection. It then takes this information and 
    # places that data in a temporary book function that the template can access and retrieve without the use of the API. 
    def getDNF(self):
        self.cursor.execute("SELECT B.ImageURL, B.Title, B.Pages, BC.UserRating FROM Book AS B INNER JOIN BookInUserCollection as BC ON B.APIid = BC.ISBN AND BC.shelfName = 'DNF' AND BC.Email = %s;", [self.email])
        tupleInfo = self.cursor.fetchall()
        list = []
        print(tupleInfo)
        for i in range(len(tupleInfo)):
            book = BookModel.BookModel()
            book.bookImg = tupleInfo[i][0]
            book.title = tupleInfo[i][1]
            book.pageCount = tupleInfo[i][2]
            book.userRating = tupleInfo[i][3]
            list.append(book)

        return list