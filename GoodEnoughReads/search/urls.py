from django.urls import path
from . import viewsSearch
from Collections import views


urlpatterns = [
    path('search/', viewsSearch.search, name = "search"),
    path('toRead/<bookID>', views.toRead, name = "toRead"),
    path('bookDisplay/', viewsSearch.bookDisplay, name = "bookDisplay"),
    path('bookDisplayFromCollection/', viewsSearch.bookDisplayFromCollection, name = "bookDisplayFromCollection"),
    path('bookInfo/', viewsSearch.bookInfo, name = "bookInfo"),
    path('bookSubmission/', viewsSearch.bookSubmission, name = "bookSubmission"),
    path('bookSubmissionFromCollection/', viewsSearch.bookSubmissionFromCollection, name = "bookSubmissionFromCollection"),
    path('bookSubmissionToRead/', viewsSearch.bookSubmissionToRead, name = "bookSubmissionToRead")
]

