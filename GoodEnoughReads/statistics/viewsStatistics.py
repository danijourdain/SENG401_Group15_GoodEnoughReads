from django.shortcuts import render, redirect

def statistics(request):
    return render(request, 'statistics/statistics.html',{})