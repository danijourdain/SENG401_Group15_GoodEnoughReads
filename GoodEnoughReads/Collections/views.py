from django.shortcuts import render, redirect
from django.contrib.auth import logout

def collection(request):
    return render(request, 'Collections/collection.html')

def read(request):
    return render(request, 'Collections/read.html')

def toRead(request, bookID = "default"):
    context = {"bookID": bookID}
    return render(request, 'Collections/toRead.html', context)

def currentlyReading(request):
    return render(request, 'Collections/collection.html')

def DNF(request):
    return render(request, 'Collections/collection.html')