# this is an automated file updated by Ryan Mailhiot and Maitry Rohit
# Last modified March 23, 2023
from django.urls import path
from . import viewsSearch
from Collections import views

# These are redirection urls for when the controller is looking for where to send information.
urlpatterns = [
    path('search/', viewsSearch.search, name = "search"),
    path('toRead/<bookID>', views.toRead, name = "toRead"), # unused in its current capacity but can be used later if needed
    path('bookDisplay/', viewsSearch.bookDisplay, name = "bookDisplay"),
    path('bookDisplayFromCollection/', viewsSearch.bookDisplayFromCollection, name = "bookDisplayFromCollection"),
    path('bookInfo/', viewsSearch.bookInfo, name = "bookInfo"),
    path('bookSubmission/', viewsSearch.bookSubmission, name = "bookSubmission"),
    path('bookSubmissionFromCollection/', viewsSearch.bookSubmissionFromCollection, name = "bookSubmissionFromCollection"),
    path('bookSubmissionToRead/', viewsSearch.bookSubmissionToRead, name = "bookSubmissionToRead")
]

