from django.shortcuts import render, redirect
from django.contrib.auth import logout
from . import CollectionModel
from search import BookModel


collections = CollectionModel.CollectionModel()

def collection(request):
    email = request.session['email']
    collections.setEmail(email)
    bookList = collections.getAllCollection()

    context = {
        'bookList': bookList,
        'path': request.get_full_path(),
        }
    return render(request, 'Collections/collection.html', context)

def read(request):
    email = request.session['email']
    collections.setEmail(email)
    bookList = collections.getRead()

    context = {
        'bookList': bookList,
        'path': request.get_full_path(),
        }
    return render(request, 'Collections/read.html', context)

def toRead(request, bookID = "default"):
    email = request.session['email']
    collections.setEmail(email)
    bookList = collections.gettoRead()

    context = {
        'bookList': bookList,
        'path': request.get_full_path(),
        }
    return render(request, 'Collections/toRead.html', context)

def currentlyReading(request):
    email = request.session['email']
    collections.setEmail(email)
    bookList = collections.getcurrentlyReading()

    context = {
        'bookList': bookList,
        'path': request.get_full_path(),
        }
    return render(request, 'Collections/currentlyReading.html', context)

def DNF(request):
    email = request.session['email']
    collections.setEmail(email)
    bookList = collections.getDNF()

    context = {
        'bookList': bookList,
        'path': request.get_full_path(),
        }
    return render(request, 'Collections/dnf.html', context)

def removeBook(request):
    bookID = request.POST.get("bookrmv", '')
    path = request.POST.get("bookPath", '')
    collections.removeBook(bookID)
    return redirect(path)
    