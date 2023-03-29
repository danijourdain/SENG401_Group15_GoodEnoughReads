from django.db import models
from django.db import connection, transaction
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
# import requests
from datetime import datetime

# The book model makes saving components the user searches for possible.
# The important part of this class is the translation between MySQL and Models which happens within a given function
# Variable names will have details if needed
class BookModel():
    def __init__(self):
        self.title = None 
        self.author = None # Multiple authors are not stored
        self.publisher = None # Multiple publishers are not stored
        self.bookImg = None
        self.pageCount = 0 # 0 by default. Will always contain a value from google books API (0 page books are removed)
        self.maxPages = 0 
        self.desc = None # Description from the google books API
        self.rating = 0 # This is google books API rating. Can come in as undefined which gets translated to 0
        self.userRating = 0 # This is what the user rates the book
        self.startDate = None # dates are for statistics tracking
        self.endDate = None
        self.bookID = None # used as primary key
        self.genre = None # only stored from OpenLibraryAPI. Google Books API is too unreliable for genre data
        self.shelf = None
        self.email = None
        self.timesRead = 0
        self.cursor = connection.cursor()

    # used in bookDisplay function in viewsSearch.py.
    # This stores the information for a book when the user selects it from the search page
    def set(self, title, author, publisher, bookImg, pageCount, desc, rating, bookID, email):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.bookImg = bookImg
        self.pageCount = pageCount
        self.maxPages = pageCount
        self.desc = desc
        if rating == "unavailable": # if rating is undefined from google books API it gets translated to a string
                                    # This happens in search.js.
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

    # this is used in bookSubmission and bookSubmissionToRead in viewsSearch.py.
    # Normally followed by addBooktoBooksinUserCollection()
    def setInfo(self, startDate, endDate, rating, timesRead, shelf, pagesRead):
        self.shelf = shelf
        self.startDate = startDate
        self.endDate = endDate
        self.userRating = rating
        self.timesRead = timesRead
        self.pageCount = pagesRead

    # this selects the title and book image stored in the database for a given book
    # Used in bookDisplayFromCollection in viewsSearch.py    
    def retrieveBook(self, bookID):
        self.bookID = bookID
        self.cursor.execute('SELECT title, ImageURL FROM Book WHERE APIid = %s', [self.bookID])
        val = self.cursor.fetchone()
        self.title = val[0]
        self.bookImg = val[1]

    # this is used in bookDisplay in viewsSearch.py.
    # it is called after set()
    def addBooktoBooks(self):
        self.cursor.execute('SELECT * FROM Book WHERE Book.APIid = %s', [self.bookID])
        val = self.cursor.fetchall()
        print(val)
        
        # Val can be 2 things:
            # 1. A tuple is found and therefore the book exists in the database
            # 2. A tuple is not found and therefore does not exist in the database - This means that val = None
        
        if not val: #if val = None then you can insert
            self.cursor.execute('INSERT INTO Book(APIid, ImageURL, Title, Genre, Pages, Rating) VALUES(%s, %s, %s, %s, %s, %s)', (self.bookID, self.bookImg, self.title, self.genre, self.maxPages, self.rating))
        
        elif self.bookID in val[0]: # the bookID we are about to add already exists in the database therefore we don't need to add it and can return back
           return
        
        else: # I'm honestly not sure why this is here but Im scare it will break the program if it isn't
            self.cursor.execute('INSERT INTO Book(APIid, ImageURL, Title, Genre, Pages, Rating) VALUES(%s, %s, %s, %s, %s, %s)', (self.bookID, self.bookImg, self.title, self.genre, self.maxPages, self.rating))
      
    # this is used in bookSubmission and bookSubmissionToRead in viewsSearch.py.
    # called after setInfo()
    def addBooktoBooksinUserCollection(self):
        start = None
        end = None
        self.cursor.execute('SELECT * FROM BookInUserCollection WHERE ISBN = %s and Email = %s;', [self.bookID, self.email])
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
    
    # This is used in bookInfo in viewsSearch.py
    def checkBookInUserCollection(self, email):
        self.email = email
        self.cursor.execute('SELECT * FROM BookInUserCollection WHERE ISBN = %s and Email = %s;', [self.bookID, self.email])
        val = self.cursor.fetchall()

        # Val can be 2 things:
            # 1. A tuple is found and therefore the book exists in the users collection already - A user wants to edit the book information in this case
            # 2. A tuple is not found and therefore does not exist in the database - This means that val = None
        if not val: #if val = None then you can insert
            return False
        
        elif self.bookID in val[0]: # the bookID we are about to add already exists in the database therefore we don't need to add it and can return back
            return True
        
    # this is used in bookInfo and bookSubmissionFromCollection in viewsSearch.py
    # This will grab information based on the user and book from a given collection and set the book info
    # to be transfered into a template for bookInfo.html
    # basically a data structure setting from information in the database
    def setInfoFromDataBase(self):
        self.cursor.execute('SELECT * FROM BookInUserCollection WHERE BookInUserCollection.ISBN = %s and Email = %s', [self.bookID, self.email])
        val = self.cursor.fetchall()

        self.shelfName = val[0][6]
        print(self.shelfName)
        print(val)
        self.startDate = None
        self.endDate = None
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
        