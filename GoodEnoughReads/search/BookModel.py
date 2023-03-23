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
        if rating == "unavailable":
            self.rating = 0
        else:
            self.rating = rating
        self.bookID = bookID
        self.email = email
        print(bookID)
        print(rating)
        print(bookImg)

    def setInfo(self, startDate, endDate, rating, reread, shelf):
        self.shelf = shelf
        self.startDate = startDate
        self.endDate = endDate
        self.userRating = rating
        self.reread = reread

    def addBooktoBooks(self):
        self.cursor.execute('SELECT * FROM Book WHERE Book.APIid = %s', [self.bookID])
        val = self.cursor.fetchall()
        print(val)
        if not val:
            self.cursor.execute('INSERT INTO Book(APIid, ImageURL, Title, Genre, Pages, Rating) VALUES(%s, %s, %s, %s, %s, %s)', (self.bookID, self.bookImg, self.title, self.genre, self.pageCount, self.rating))
        elif self.bookID in val[0]:
            return
        else:
            self.cursor.execute('INSERT INTO Book(APIid, ImageURL, Title, Genre, Pages, Rating) VALUES(%s, %s, %s, %s, %s, %s)', (self.bookID, self.bookImg, self.title, self.genre, self.pageCount, self.rating))
      

    def addBooktoBooksinUserCollection(self):
        start = None
        end = None
        if(self.shelf != 'toRead'):
            start = datetime.strptime(self.startDate,'%Y-%m-%d').date()
            end = datetime.strptime(self.endDate,'%Y-%m-%d').date()
        
        print("SOMEONE TELL ME WHAT IN THE WORLD IS HAPPENING")
        print(self.shelf)
        print(self.bookID)


        self.cursor.execute("INSERT INTO BookInUserCollection(UserRating, NewestReadingStartDate, NewestReadingEndDate, NumberOfTimesReread, PagesRead, ISBN, Email, shelfName) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", 
                            (int(self.userRating), start, end, int(self.reread), int(self.pageCount), self.bookID, self.email, self.shelf))
    

