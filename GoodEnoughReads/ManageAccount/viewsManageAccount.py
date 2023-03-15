from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from gersiteapp import LoginModel

def logout_view(request):
    return redirect('login')

# def login(request):
#     return render(request, 'ManageAccount/registration/login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        uname = request.POST.get('username', '')
        pw1 = request.POST.get('password', '')
        pw2 = request.POST.get('password2', '')
        user = authenticate(request, email=email)
        
        login = LoginModel.LoginModel(email)
        uniqueEmail = login.verifyUser()
        if not uniqueEmail:
            error_message = "That email is already signed up!"
            # template currently not made
            return render(request, 'ManageAccount/signup.html', {'error_message': error_message})

        if user is None and pw1 == pw2:
            user = User.objects.create_user(username=uname, password=pw1, email=email)
            user.first_name = fname
            user.last_name = lname
            user.save()
            login.signupUser()
            
            context = {'username': uname}
            return redirect('/welcome/', context)
        else:
            error_message = "Invalid login credentials"
            return render(request, 'ManageAccount/signup.html', {'error_message': error_message})
    else:
        return render(request, 'ManageAccount/signup.html')

def reset_password(request):
    return render(request, 'ManageAccount/reset_password.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            context = {'username': username}
            return render(request, 'gersiteapp/welcome.html', context)
        else:
            error_message = "Invalid login credentials"
            return render(request, 'ManageAccount/registration/login.html', {'error_message': error_message})
    else:
        return render(request, 'ManageAccount/registration/login.html')
    