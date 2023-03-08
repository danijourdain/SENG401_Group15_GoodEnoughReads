from django.shortcuts import render, redirect
from django.contrib.auth import logout

def logout_view(request):
    return redirect('login')

def login(request):
    return render(request, 'ManageAccount/login.html')

def signup(request):
    return render(request, 'ManageAccount/signup.html')

def reset_password(request):
    return render(request, 'ManageAccount/reset_password.html')
