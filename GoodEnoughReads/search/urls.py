from django.urls import path
from . import viewsSearch
from Collections import views


urlpatterns = [
    path('search/', viewsSearch.search, name = "search"),
    path('toRead/<bookID>', views.toRead, name = "toRead"),
    path('bookDisplay/', viewsSearch.bookDisplay, name = "bookDisplay"),
    path('bookInfo/', viewsSearch.bookInfo, name = "bookInfo"),
    path('bookSubmission/', viewsSearch.bookSubmission, name = "bookSubmission")
]

