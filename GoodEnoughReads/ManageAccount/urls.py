from django.urls import path, include
from . import viewsManageAccount

urlpatterns = [
    path('', viewsManageAccount.login, name='login'),
    path('login/', viewsManageAccount.login, name='login'),
    path('logout/', viewsManageAccount.logout_view, name='logout'),
    path('signup/', viewsManageAccount.signup, name='signup'),
    path('reset-password/', viewsManageAccount.reset_password, name='reset_password'),
    path('account/', viewsManageAccount.account, name='account'),
]