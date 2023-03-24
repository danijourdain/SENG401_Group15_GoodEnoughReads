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


# There are 2 options for when a user wants to add a book into their shelf
# 1. The book does not exist anywhere in the collection 
# 2. The book already exists in the collection and the user wants to edit the book
    # - When the book already exists in the users collection it retrieves the information rather than having empty
    # - This way a user does not need to remember they previously gave
def bookInfo(request):
    check = book.checkBookInUserCollection()
    if check:
        book.setInfoFromDataBase()

    dateM = datetime.datetime.now()
    dateString = dateM.strftime('%Y-%m-%d')
    context = {
        "dateMax": dateString, 
        "book": book
    }
    return render(request, 'search/bookInfo.html', context)

def bookSubmission(request):
    shelf = request.POST.get("shelf", "")
    startDate = request.POST.get("startDate", "")
    endDate = request.POST.get("endDate", "")
    ratingUser = request.POST.get("rating", "")
    timesRead = request.POST.get("timesRead","")

    start = datetime.datetime.strptime(startDate,'%Y-%m-%d').date()
    end = datetime.datetime.strptime(endDate,'%Y-%m-%d').date()
    
    if start > end:
        return redirect('/bookInfo/')
    
    book.setInfo(startDate, endDate, ratingUser, timesRead, shelf)
    book.addBooktoBooksinUserCollection()
    return redirect('/search/')

def bookSubmissionToRead(request):
    shelf = 'toRead'
    startDate = None
    endDate = None
    ratingUser = 0
    timesRead = 0
    
    book.setInfo(startDate, endDate, ratingUser, timesRead, shelf)
    book.addBooktoBooksinUserCollection()
    return redirect('/search/')
   




