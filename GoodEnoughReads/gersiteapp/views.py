from django.shortcuts import render, redirect
from django.contrib.auth import logout
import requests
from . import LoginModel

def welcome(request):
    # Make API call to Open Library to retrieve books by genre
    genre = 'fiction'
    url = f'https://openlibrary.org/subjects/{genre}.json'
    response = requests.get(url)
    data = response.json()

    # Extract information about books and their covers
    books = []
    for work in data['works']:
        book = {}
        book['title'] = work['title']
        book['author'] = work['authors'][0]['name']
        book['cover'] = f'https://covers.openlibrary.org/b/id/{work["cover_id"]}-M.jpg'
        books.append(book)

    return render(request, 'gersiteapp/welcome.html', {'books': books})

def shelf(request):
    return render(request, 'gersiteapp/shelf.html')

def bookshelf(request):
    return render(request, 'gersiteapp/bookshelf.html')

# def account(request):
#     return render(request, 'gersiteapp/account.html')

# def statistics(request):
#     return render(request, 'gersiteapp/statistics.html')

# def settings(request):
#     return render(request, 'gersiteapp/settings.html')

def recommendations(request):
    return render(request, 'gersiteapp/recommendations.html')