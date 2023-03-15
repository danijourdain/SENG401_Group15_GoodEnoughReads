from django.shortcuts import render, redirect
from . import Awards

def awards(request):
    return render(request, 'Awards/awards.html', {})
