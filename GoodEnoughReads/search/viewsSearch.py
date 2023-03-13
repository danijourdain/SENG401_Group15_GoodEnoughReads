from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

def search(request):
    return render(request, 'search/search.html',{})

@csrf_exempt
def bookDisplay(request):
    title = request.POST.get('title', '')
    author = request.POST.get('author', '')
    publisher = request.POST.get('publisher', '')
    bookImg = request.POST.get('bookImg', '')
    pageCount = request.POST.get('pageCount', '')

    context = {
        "title": title,
        "author": author,
        "publisher": publisher,
        "bookImg": bookImg,
        "pageCount": pageCount
    }
    return render(request, 'search/bookDisplay.html', context)