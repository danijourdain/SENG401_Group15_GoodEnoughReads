from django.shortcuts import render, redirect
from django.contrib.auth import logout
import requests
from . import LoginModel
from datetime import datetime
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def welcome(request):
    genres = ['fiction', 'romance', 'thriller', 'mystery', 'fantasy', 'science-fiction']
    if 'shuffled_books' in request.session:
        books = request.session['shuffled_books']
    else:

        books = []
        for genre in genres:
            url = f'https://openlibrary.org/subjects/{genre}.json?limit=15'
            response = requests.get(url)
            data = response.json()
            for work in data['works']:
                title = work['title']
                author = work['authors'][0]['name']
                cover_id = work['cover_id']
                cover_url = f'https://covers.openlibrary.org/b/id/{cover_id}-M.jpg'
                if any(b['title'] == title and b['author'] == author for b in books):
                    continue  
                book = {'title': title, 'author': author, 'cover': cover_url, 'genre': genre.capitalize()}
                books.append(book)
        random.seed()
        random.shuffle(books)
        request.session['shuffled_books'] = books

    now = datetime.now()
    time_of_day = ''
    if 5 <= now.hour < 12:
        time_of_day = 'Good morning,'
    elif 12 <= now.hour < 18:
        time_of_day = 'Good afternoon, '
    elif 18 <= now.hour < 23:
        time_of_day = 'Good evening, '
    else:
        time_of_day = 'Up late are we, '

    paginator = Paginator(books, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gersiteapp/welcome.html', {'books': page_obj, 'greeting': time_of_day})

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