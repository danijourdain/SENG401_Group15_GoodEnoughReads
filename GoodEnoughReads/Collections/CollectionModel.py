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
        self.cursor.execute("INSERT INTO BookInUserCollection VALUES ("+startdate+", "+enddate+", "+pagesread+", "+isbn+", '"+email+"');")
        
    def getName(self):
        self.cursor.execute("SELECT Name FROM Collection WHERE Email = '" + self.email + "' ;")
        return self.cursor.fetchall()[0]
    
    def getBooksInCollection(self, shelfName):
        self.cursor.execute("SELECT ISBN FROM BookInUserCollection WHERE Email = '"+self.email+"';")
        bookList = self.cursor.fetchall()
        return bookList
    
    # user passes in a book, gets every collection of theirs with said book
    def collectionsWithBook(self, bookisbn):
        self.cursor.execute("SELECT ShelfName FROM BookInUserCollection WHERE Email = '"+self.email+"' AND ISBN = "+bookisbn+";")
        cols = self.cursor.fetchall()
        return cols
    
    def getAllCollection(self):
        self.cursor.execute("SELECT B.ImageURL, B.Title, B.Pages, BC.UserRating FROM Book AS B INNER JOIN BookInUserCollection as BC ON B.APIid = BC.ISBN AND BC.Email = '"+self.email+"';")
        tupleInfo = self.cursor.fetchall()
        print("HELP ME PLEASE FOR THE LOVE OF GOD HELP ME IM_")
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
    
    def getRead(self):
        self.cursor.execute("SELECT B.ImageURL, B.Title, B.Pages, BC.UserRating FROM Book AS B INNER JOIN BookInUserCollection as BC ON B.APIid = BC.ISBN AND BC.shelfName = 'read' AND BC.Email = '"+self.email+"';")
        tupleInfo = self.cursor.fetchall()
        print("HELP ME PLEASE FOR THE LOVE OF GOD HELP ME IM_")
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
    
    def gettoRead(self):
        self.cursor.execute("SELECT B.ImageURL, B.Title, B.Pages, BC.UserRating FROM Book AS B INNER JOIN BookInUserCollection as BC ON B.APIid = BC.ISBN AND BC.shelfName = 'toRead' AND BC.Email = '"+self.email+"';")
        tupleInfo = self.cursor.fetchall()
        print("HELP ME PLEASE FOR THE LOVE OF GOD HELP ME IM_")
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
    
    def gettoRead(self):
        self.cursor.execute("SELECT B.ImageURL, B.Title, B.Pages, BC.UserRating FROM Book AS B INNER JOIN BookInUserCollection as BC ON B.APIid = BC.ISBN AND BC.shelfName = 'curentlyReading' AND BC.Email = '"+self.email+"';")
        tupleInfo = self.cursor.fetchall()
        print("HELP ME PLEASE FOR THE LOVE OF GOD HELP ME IM_")
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
    
    def getDNF(self):
        self.cursor.execute("SELECT B.ImageURL, B.Title, B.Pages, BC.UserRating FROM Book AS B INNER JOIN BookInUserCollection as BC ON B.APIid = BC.ISBN AND BC.shelfName = 'DNF' AND BC.Email = '"+self.email+"';")
        tupleInfo = self.cursor.fetchall()
        print("HELP ME PLEASE FOR THE LOVE OF GOD HELP ME IM_")
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