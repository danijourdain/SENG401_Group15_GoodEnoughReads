from django.shortcuts import render, redirect
from . import StatisticsModel

def statistics(request):

    stats = StatisticsModel.StatisticsModel("a@gmail.com")
    pages_this_week = stats.NumPagesThisWeek()
    
    books_this_month, books_per_month = stats.CalculateBooksPerMonth()
    stats.CreateBarGraph(list(books_per_month.keys()), list(books_per_month.values()), "Months", "Number of Books Read", "Number of Books you Read per Month this Year")
    
    books_this_year, books_per_year = stats.CalculateBooksPerYear()
    stats.CreateLineGraph(list(books_per_year.keys()), list(books_per_year.values()), "Year", "Number of Books Read", "All Time Number of Books you Read")
    
    genres_this_year = stats.CalculateGenresPerYear()
    stats.CreatePieChart(list(genres_this_year.keys()), list(genres_this_year.values()), "Genres you Read this year")

    book_pages_this_year = stats.CalculateBookPagesPerYear()
    stats.CreatePieChart(list(book_pages_this_year.keys()), list(book_pages_this_year.values()), "Book Pages you Read this year")

    books_reread_the_most = stats.CalcBookReread()

    return render(request, 'Statistics/statistics.html', {'pages_this_week': pages_this_week, 
                                                          'books_this_month': books_this_month,
                                                          'books_this_year': books_this_year,
                                                          'books_reread': books_reread_the_most})