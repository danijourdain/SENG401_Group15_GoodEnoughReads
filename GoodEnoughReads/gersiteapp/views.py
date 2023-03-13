from django.shortcuts import render, redirect
from django.contrib.auth import logout
from . import LoginModel

def welcome(request):
    return render(request, 'gersiteapp/welcome.html')

def shelf(request):
    return render(request, 'gersiteapp/shelf.html')

def bookshelf(request):
    return render(request, 'gersiteapp/bookshelf.html')

def account(request):
    return render(request, 'gersiteapp/account.html')

# def statistics(request):
#     return render(request, 'gersiteapp/statistics.html')

def settings(request):
    return render(request, 'gersiteapp/settings.html')

def recommendations(request):
    return render(request, 'gersiteapp/recommendations.html')