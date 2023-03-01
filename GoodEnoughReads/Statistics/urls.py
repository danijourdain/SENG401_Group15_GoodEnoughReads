from django.urls import path
from . import viewsStatistics
urlpatterns = [
    path('statistics/', viewsStatistics.statistics, name = 'statistics'),
]
