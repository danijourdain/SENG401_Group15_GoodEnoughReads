from django.urls import path, include
from . import views

urlpatterns = [
    path('read/', views.read, name='read'),
    path('toRead/', views.toRead, name='toRead'),
    path('currentlyReading/', views.currentlyReading, name='currentlyReading'),
    path('dnf/', views.DNF, name='dnf'),
    path('collection/', views.collection, name='collection'),
    #path("collection/", include("Collections.urls")),
]

