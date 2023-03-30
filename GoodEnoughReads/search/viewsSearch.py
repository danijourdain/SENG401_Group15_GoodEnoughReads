# This is a file created by Ryan Mailhiot and Maitry Rohit.
# Last modified date: March 29, 2023

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import BookModel
import datetime

#import datetime

book = BookModel.BookModel()

def search(request):
    return render(request, 'search/search.html')

#Book information that is returned from the API itself 
# - Data cannot be corrupted because its not user input
#This is called from the search page directly using the hidden form in search.js
@csrf_exempt
def bookDisplay(request, ):
    title = request.POST.get('title', '')
    author = request.POST.get('author', '')
    publisher = request.POST.get('publisher', '')
    bookImg = request.POST.get('bookImg', '')
    pageCount = request.POST.get('pageCount', '')
    desc = request.POST.get('desc', '')
    rating = request.POST.get('rating', '')
    bookID = request.POST.get('bookID', '')
    context = {
        "title": title,
        "author": author,
        "publisher": publisher,
        "bookImg": bookImg,
        "pageCount": pageCount,
        "desc": desc,
        "rating": rating,
        "bookID": bookID
    }
    email = request.session['email']
    book.set(title, author, publisher, bookImg, pageCount, desc, rating, bookID, email)
    book.addBooktoBooks()
    return render(request, 'search/bookDisplay.html', context)

# calls the bookDisplay.html file after retrieving information from the database
# This comes from collections
def bookDisplayFromCollection(request):
    bookID = request.POST.get('bookdisp', '')
    book.retrieveBook(bookID)
    context = {
        "title": book.title,
        "author": book.author,
        "publisher": book.publisher,
        "bookImg": book.bookImg,
        "pageCount": book.pageCount,
        "desc": book.desc,
        "rating": book.rating,
        "bookID": bookID
    }

    return render(request, 'search/bookDisplay.html', context)


# There are 2 options for when a user wants to add a book into their shelf
# 1. The book does not exist anywhere in the collection 
# 2. The book already exists in the collection and the user wants to edit the bookInfo
    # - When the book already exists in the users collection it retrieves the information rather than having empty
    # - This way a user does not need to remember they previously gave
def bookInfo(request):
    email = request.session['email']
    check = book.checkBookInUserCollection(email)
    if check:
        book.setInfoFromDataBase()

    dateM = datetime.datetime.now()
    dateString = dateM.strftime('%Y-%m-%d')
    context = {
        "dateMax": dateString, 
        "book": book
    }
    return render(request, 'search/bookInfo.html', context)

# This submits a book to the database for a given collection with all the fields input. 
def bookSubmission(request):
    start = None
    end = None
    shelf = request.POST.get("shelf", "") # Shelf is also collection. 
    startDate = request.POST.get("startDate", "")
    endDate = request.POST.get("endDate", "")
    ratingUser = request.POST.get("rating", "")
    timesRead = request.POST.get("timesRead","")
    pagesRead = request.POST.get("pagesRead", '')

    if shelf == 'toRead': # If shelf is toRead, dont worry about anything
        bookSubmissionToRead(request)

    if  not startDate == "":
        start = datetime.datetime.strptime(startDate,'%Y-%m-%d').date()
    
    if not endDate == "":
        end = datetime.datetime.strptime(endDate,'%Y-%m-%d').date()
    
    if (not endDate == "") and (not startDate == ""):
        if start > end:
            return redirect('/bookInfo/') # retry if invalid input
    
    book.setInfo(startDate, endDate, ratingUser, timesRead, shelf, pagesRead)
    book.addBooktoBooksinUserCollection()
    return redirect('/collection/')

# This runs the bookInfo.html file and receives information from collections. 
# This happens if a request comes from collections
def bookSubmissionFromCollection(request):
    book.bookID = request.POST.get("booksubmit", "")
    book.email = request.session['email']
    book.setInfoFromDataBase()
    dateM = datetime.datetime.now()
    dateString = dateM.strftime('%Y-%m-%d')
    context = {
        "dateMax": dateString, 
        "book": book
    }
    return render(request, 'search/bookInfo.html', context)
# This submits data the to read collection. Because the user is storing it for later and has not read the book,
# regardless of the information they put on the submission form, none of it will be stored.
def bookSubmissionToRead(request):
    shelf = 'toRead'
    startDate = None
    endDate = None
    ratingUser = 0
    timesRead = 0
    pagesRead = 0
    
    book.setInfo(startDate, endDate, ratingUser, timesRead, shelf, pagesRead)
    book.addBooktoBooksinUserCollection()
    return redirect('/search/')
   




