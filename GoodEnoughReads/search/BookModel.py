from django.db import models
from django.db import connection, transaction
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
# import requests
from datetime import datetime


class BookModel():
    def __init__(self):
        self.title = None
        self.author = None
        self.publisher = None
        self.bookImg = None
        self.pageCount = 0
        self.desc = None
        self.rating = 0
        self.userRating = 0
        self.startDate = None
        self.endDate = None
        self.bookID = None
        self.genre = None
        self.shelf = None
        self.email = None
        self.cursor = connection.cursor()

    def set(self, title, author, publisher, bookImg, pageCount, desc, rating, bookID, email):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.bookImg = bookImg
        self.pageCount = pageCount
        self.desc = desc
        self.rating = rating
        self.bookID = bookID
        self.email = email
        print(bookID)

    def setInfo(self, startDate, endDate, rating, reread, shelf):
        self.shelf = shelf
        self.startDate = startDate
        self.endDate = endDate
        self.userRating = rating
        self.reread = reread

    def addBooktoBooks(self):
        self.cursor.execute('INSERT INTO Book(APIid, Title, Genre, Pages, Rating) VALUES(%s, %s, %s, %s, %s)', (self.bookID, self.title, self.genre, self.pageCount, self.rating))

    def addBooktoBooksinUserCollection(self):
        start = datetime.strptime(self.startDate,'%Y-%m-%d').date()
        end = datetime.strptime(self.endDate,'%Y-%m-%d').date()
        print(self.shelf)
        print(self.bookID)
        # print(ISBN)
        # self.cursor.execute("""INSERT INTO BookInUserCollection(UserRating, NewestReadingStartDate, 
        #                     NewestReadingEndDate, NumberOfTimesReread, PagesRead, ISBN, Email, CollectionID) VALUES(%s,'%s','%s',%s, %s, %s,%s, %s)""", 
        #                     (int(self.userRating), start, end, int(self.reread), int(self.pageCount), ISBN, email, 1,))

        self.cursor.execute("INSERT INTO BookInUserCollection(UserRating, NewestReadingStartDate, NewestReadingEndDate, NumberOfTimesReread, PagesRead, ISBN, Email, CollectionName) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", 
                            (int(self.userRating), start, end, int(self.reread), int(self.pageCount), self.bookID, self.email, self.shelf))
    

