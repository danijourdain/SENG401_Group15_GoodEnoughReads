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
        self.maxPages = 0
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
        self.maxPages = pageCount
        self.desc = desc
        if rating == "unavailable":
            self.rating = 0
        else:
            self.rating = rating
        self.bookID = bookID
        self.email = email
        self.startDate = None
        self.endDate = None
        print(bookID)
        print(rating)
        print(bookImg)

    def setInfo(self, startDate, endDate, rating, timesRead, shelf):
        self.shelf = shelf
        self.startDate = startDate
        self.endDate = endDate
        self.userRating = rating
        self.timesRead = timesRead

    def retrieveBook(self, bookID):
        self.bookID = bookID
        self.cursor.execute('SELECT * FROM Book WHERE APIid = %s', [self.bookID])

    def addBooktoBooks(self):
        self.cursor.execute('SELECT * FROM Book WHERE Book.APIid = %s', [self.bookID])
        val = self.cursor.fetchall()
        print(val)
        
        # Val can be 2 things:
            # 1. A tuple is found and therefore the book exists in the database
            # 2. A tuple is not found and therefore does not exist in the database - This means that val = None
        
        if not val: #if val = None then you can insert
            self.cursor.execute('INSERT INTO Book(APIid, ImageURL, Title, Genre, Pages, Rating) VALUES(%s, %s, %s, %s, %s, %s)', (self.bookID, self.bookImg, self.title, self.genre, self.pageCount, self.rating))
        
        elif self.bookID in val[0]: # the bookID we are about to add already exists in the database therefore we don't need to add it and can return back
           return
        
        else: # I'm honestly not sure why this is here but Im scare it will break the program if it isn't
            self.cursor.execute('INSERT INTO Book(APIid, ImageURL, Title, Genre, Pages, Rating) VALUES(%s, %s, %s, %s, %s, %s)', (self.bookID, self.bookImg, self.title, self.genre, self.pageCount, self.rating))
      

    def addBooktoBooksinUserCollection(self):
        start = None
        end = None
        self.cursor.execute('SELECT * FROM BookInUserCollection WHERE BookInUserCollection.ISBN = %s and Email = %s', [self.bookID, self.email])
        val = self.cursor.fetchall()

        print(self.bookID)
        # Val can be 2 things:
            # 1. A tuple is found and therefore the book exists in the users collection already - A user wants to edit the book information in this case
            # 2. A tuple is not found and therefore does not exist in the database - This means that val = None
        if not val: #if val = None then you can insert
            pass
        
        elif self.bookID in val[0]: # the bookID we are about to add already exists in the database therefore we don't need to add it and can return back
            self.cursor.execute('DELETE FROM BookInUserCollection WHERE ISBN = %s AND Email = %s;', [self.bookID, self.email] )
        
        if  self.startDate != "" and self.startDate != None:
            start = datetime.strptime(self.startDate,'%Y-%m-%d').date()
    
        if self.endDate != "" and self.endDate != None:
            end = datetime.strptime(self.endDate,'%Y-%m-%d').date()
    
        self.cursor.execute("INSERT INTO BookInUserCollection(UserRating, NewestReadingStartDate, NewestReadingEndDate, NumberOfTimesReread, PagesRead, ISBN, Email, shelfName) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", 
                            (int(self.userRating), start, end, int(self.timesRead), int(self.pageCount), self.bookID, self.email, self.shelf))
    

    def checkBookInUserCollection(self):
        self.cursor.execute('SELECT * FROM BookInUserCollection WHERE BookInUserCollection.ISBN = %s and Email = %s', [self.bookID, self.email])
        val = self.cursor.fetchall()

        # Val can be 2 things:
            # 1. A tuple is found and therefore the book exists in the users collection already - A user wants to edit the book information in this case
            # 2. A tuple is not found and therefore does not exist in the database - This means that val = None
        
        if not val: #if val = None then you can insert
            return False
        
        elif self.bookID in val[0]: # the bookID we are about to add already exists in the database therefore we don't need to add it and can return back
            return True
    
    def setInfoFromDataBase(self):
        self.cursor.execute('SELECT * FROM BookInUserCollection WHERE BookInUserCollection.ISBN = %s and Email = %s', [self.bookID, self.email])
        val = self.cursor.fetchall()

        print("WHERE AM I?")
        self.shelfName = val[0][6]
        print(self.shelfName)
        print(val)

        if val[0][1] != None:
            self.startDate = (val[0][1]).strftime('%Y-%m-%d')
        
        if val[0][2] != None:
            self.endDate = (val[0][2]).strftime('%Y-%m-%d')

        self.userRating = val[0][0]
        self.timesRead = val[0][3]
        self.pageCount = val[0][4]

        self.cursor.execute('SELECT ImageURL, Title, Pages FROM Book WHERE Book.APIid = %s', [self.bookID])
        val = self.cursor.fetchall()
        self.bookImg = val[0][0]
        self.title = val[0][1]
        self.maxPages = val[0][2]
        




