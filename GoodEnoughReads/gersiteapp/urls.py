from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('read/', views.read, name='read'),
    path('to_read/', views.to_read, name='to_read'),
    path('shelf/', views.shelf, name='shelf'),
    path('bookshelf/', views.bookshelf, name='bookshelf'),
    path('search/', views.search, name='search'),
    path('collection/', views.collection, name='collection'),
    path('account/', views.account, name = 'account'),   
    path('statistics/', views.statistics, name='statistics'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout_view, name='logout'),
    path('recommendations/', views.recommendations, name='recommendations')
]

