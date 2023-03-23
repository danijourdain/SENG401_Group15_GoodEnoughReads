from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import BookModel
import datetime

#import datetime

book = BookModel.BookModel()

def search(request):
    return render(request, 'search/search.html')

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

def bookInfo(request):
    dateM = datetime.datetime.now()
    dateString = dateM.strftime('%Y-%m-%d')
    context = {
        "title": book.title,
        "bookImg": book.bookImg,
        "pagesRead": book.pageCount,
        "dateMax": dateString, 
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
   




