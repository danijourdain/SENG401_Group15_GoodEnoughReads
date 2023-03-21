from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import BookModel

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

    book.set(title, author, publisher, bookImg, pageCount, desc, rating, bookID)
    book.addBooktoBooks()
    return render(request, 'search/bookDisplay.html', context)

def bookInfo(request):
    context = {
        "title": book.title,
        "bookImg": book.bookImg,
    }
    return render(request, 'search/bookInfo.html', context)

def bookSubmission(request):
    shelf = request.POST.get("shelf", "")
    startDate = request.POST.get("startDate", "")
    endDate = request.POST.get("endDate", "")
    ratingUser = request.POST.get("rating", "")
    reread = request.POST.get("reread","")

    # print(shelf)
    # print(startDate)
    # print(endDate)
    # print(ratingUser)
    # print(reread)
    
    book.setInfo(startDate, endDate, ratingUser, reread, shelf)
    book.addBooktoBooksinUserCollection()
    return redirect('/search/')
   




