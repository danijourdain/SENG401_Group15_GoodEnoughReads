from django.urls import path
from . import viewsSearch
urlpatterns = [
    path('search/', viewsSearch.search, name = "search"),
]
