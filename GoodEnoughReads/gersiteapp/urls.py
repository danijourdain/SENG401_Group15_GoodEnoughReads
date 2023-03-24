from django.urls import path, include
from . import views
from search import viewsSearch
from Statistics import viewsStatistics
from Statistics import viewsAwards
from ManageAccount import viewsManageAccount

urlpatterns = [
    path('', viewsManageAccount.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('shelf/', views.shelf, name='shelf'),
    path('bookshelf/', views.bookshelf, name='bookshelf'),
    path('search/', viewsSearch.search, name='search'),
    path('Statistics/', viewsStatistics.statistics, name='statistics'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('Awards/', viewsAwards.awards, name='awards')
]

