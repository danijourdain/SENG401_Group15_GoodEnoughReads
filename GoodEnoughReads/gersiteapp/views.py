from django.shortcuts import render, redirect
from django.contrib.auth import logout
import requests
from datetime import datetime
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Collections import CollectionModel
from search import BookModel


def welcome(request):
    genres = ['fiction', 'romance', 'thriller', 'mystery', 'fantasy', 'science-fiction']
    if 'shuffled_books' in request.session:
        books = request.session['shuffled_books']
    else:

        books = []
        for genre in genres:
            url = f'https://openlibrary.org/subjects/{genre}.json?limit=8'
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

def recommendations(request):
    valid_genres = ['juvenile fiction', 'young adult', 'adult', 'romance', 'fantasy', 'science fiction', 'classic', 'adventure', 
                    'horror', 'mystery', 'historical fiction', 'literary fiction', 'thriller', 'crime', 'humor', 'memoir', 'biography', 'autobiography', 
                    'poetry', 'drama', 'spirituality', 'self-help', 'business', 'history', 'politics', 'science', 'travel', 'cookbooks', 'fiction', 'non-fiction', 'magical realism', 'fantasy fiction', 'comics & graphic novels manga fantasy']
    
    collection_model = CollectionModel.CollectionModel()
    email = request.session.get('email')
    if email:
        collection_model.setEmail(email)
        book_list = collection_model.getRead()
        random.shuffle(book_list)
        selected_books = book_list[0:4]
        recommended_books = []
        for book in selected_books:
            genres = get_book_genre(book.title)
            if not genres:
                continue
            valid_genres_set = set([genre.lower() for genre in valid_genres])
            book_genres = [genre for genre in genres if genre.lower() in valid_genres_set]
            if book_genres:
                similar_books = get_similar_books(book_genres, 2010)
                unique_similar_books = [sb for sb in similar_books if sb['title'].lower() != book.title.lower()]
                for book_data in unique_similar_books:
                    cover_id = book_data.get('cover_i')
                    if cover_id:
                        book_data['cover'] = f'https://covers.openlibrary.org/b/id/{cover_id}-M.jpg'
                recommended_books.append({'title': book.title, 'genres': book_genres, 'similar_books': unique_similar_books})
        return render(request, 'gersiteapp/recommendations.html', {'recommended_books': recommended_books})
    else:
        return redirect('login')

def get_book_genre(title):
    valid_genres = ['juvenile fiction', 'young adult', 'adult', 'romance', 'fantasy', 'science fiction', 'classic', 'adventure', 'horror', 'mystery']
    url = 'http://openlibrary.org/search.json'
    params = {'q': title}
    response = requests.get(url, params=params)
    book_data_list = response.json().get('docs', [])
    if not book_data_list:
        return []
    book_data = book_data_list[0]
    subjects = book_data.get('subject', [])
    genres = []
    for subject in subjects:
        if subject.lower() or subject.upper() or subject in valid_genres:
            genres.append(subject)
    return genres


def get_similar_books(genres, published_after):
    url = 'http://openlibrary.org/search.json'
    seed = str(random.random())
    params = {'subject': '|'.join(genres), 'published_in': f'>{published_after}', 'sort': 'random', 'seed': seed}
    response = requests.get(url, params=params)
    book_data_list = response.json()['docs'][:4] 
    similar_books = []
    for book_data in book_data_list:
        title = book_data.get('title', '')
        author = book_data.get('author_name', [])
        cover_id = book_data.get('cover_i', None)
        cover_url = f'https://covers.openlibrary.org/b/id/{cover_id}-M.jpg' if cover_id else None
        similar_books.append({'title': title, 'author': author, 'cover': cover_url})

    return similar_books

