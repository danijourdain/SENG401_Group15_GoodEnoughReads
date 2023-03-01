from django.urls import path, include
from . import views
from search import viewsSearch
from Statistics import viewsStatistics

urlpatterns = [
    path('', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('shelf/', views.shelf, name='shelf'),
    path('bookshelf/', views.bookshelf, name='bookshelf'),
    path('search/', viewsSearch.search, name='search'),
    path('account/', views.account, name = 'account'),   
    path('Statistics/', viewsStatistics.statistics, name='statistics'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout_view, name='logout'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('reset-password/', views.reset_password, name='reset_password'),

]

