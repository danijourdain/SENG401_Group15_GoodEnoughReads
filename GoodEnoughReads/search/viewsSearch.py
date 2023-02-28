from django.shortcuts import render, redirect

def search(request):
    return render(request, 'search/search.html',{})