from django.shortcuts import render, redirect
from django.contrib.auth import logout

def welcome(request):
    return render(request, 'gersiteapp/welcome.html')

def read(request):
    return render(request, 'gersiteapp/read.html')

def to_read(request):
    return render(request, 'gersiteapp/to_read.html')

def shelf(request):
    return render(request, 'gersiteapp/shelf.html')

def bookshelf(request):
    return render(request, 'gersiteapp/bookshelf.html')

def search(request):
    return render(request, 'gersiteapp/search.html')

def collection(request):
    return render(request, 'gersiteapp/collection.html')

def account(request):
    return render(request, 'gersiteapp/account.html')

def statistics(request):
    return render(request, 'gersiteapp/statistics.html')

def settings(request):
    return render(request, 'gersiteapp/settings.html')

def recommendations(request):
    return render(request, 'gersiteapp/recommendations.html')

def logout_view(request):
    logout(request)
    return redirect('welcome')

