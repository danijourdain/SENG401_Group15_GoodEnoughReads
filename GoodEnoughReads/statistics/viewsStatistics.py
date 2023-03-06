from django.shortcuts import render, redirect
from . import StatisticsModel

def statistics(request):

    stats = StatisticsModel.StatisticsModel("a@gmail.com")
    pages_this_week = stats.NumPagesThisWeek()
    books_per_month = stats.CalculateBooksPerMonth()
    books_per_year = stats.CalculateBooksPerYear()

    return render(request, 'Statistics/statistics.html', {'pages_this_week': pages_this_week})