from django.urls import path
from . import views
from search import viewsSearch

urlpatterns = [
    path('', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('read/', views.read, name='read'),
    path('to_read/', views.to_read, name='to_read'),
    path('shelf/', views.shelf, name='shelf'),
    path('bookshelf/', views.bookshelf, name='bookshelf'),
    path('search/', viewsSearch.search, name='search'),
    path('collection/', views.collection, name='collection'),
    path('account/', views.account, name = 'account'),   
    path('statistics/', views.statistics, name='statistics'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout_view, name='logout'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('reset-password/', views.reset_password, name='reset_password'),
]

