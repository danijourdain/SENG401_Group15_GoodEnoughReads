from django.urls import path
from . import viewsStatistics
from . import viewsAwards

urlpatterns = [
    path('statistics/', viewsStatistics.statistics, name = 'statistics'),
    path('awards/', viewsAwards.awards, name = 'awards')
]
