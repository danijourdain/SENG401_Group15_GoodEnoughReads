from django.shortcuts import render, redirect

def statistics(request):
    return render(request, 'Statistics/statistics.html')