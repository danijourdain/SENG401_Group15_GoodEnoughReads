from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from gersiteapp import LoginModel

def logout_view(request):
    auth.logout(request)
    return redirect('login')

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
            
            request.session['username'] = uname
            request.session['name'] = fname + " " + lname
            request.session['email'] = email
            return redirect('welcome')
            # return render(request, 'gersiteapp/welcome.html')
        else:
            error_message = "Invalid login credentials"
            return render(request, 'ManageAccount/signup.html', {'error_message': error_message})
    else:
        return render(request, 'ManageAccount/signup.html')

def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        uname = request.POST.get('username', '')
        pw1 = request.POST.get('password', '')
        pw2 = request.POST.get('password2', '')
        try:
            user = User.objects.get(username=uname)
        except:
            error_message = "Invalid username"
            return render(request, 'ManageAccount/reset_password.html', {'error_message': error_message})

        if user is not None and user.email == email and pw1 == pw2 and pw1 != '':
            user.set_password(pw1)
            user.save()

            request.session['username'] = uname
            request.session['name'] = user.first_name + " " + user.last_name
            request.session['email'] = user.email
            return redirect('welcome')
        else:
            error_message = "Invalid email"
            return render(request, 'ManageAccount/reset_password.html', {'error_message': error_message})
    else:
        return render(request, 'ManageAccount/reset_password.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['username'] = username
            request.session['name'] = user.first_name + " " + user.last_name
            request.session['email'] = user.email
            
            return redirect('welcome')  #why is redirect used here? i tried changing it to render but it brok everything -dani
        else:
            error_message = "Invalid login credentials"
            return render(request, 'ManageAccount/registration/login.html', {'error_message': error_message})
    else:
        return render(request, 'ManageAccount/registration/login.html')

def account(request):
    if request.method == 'POST' and request.POST.get('id') == 'updatePassword':
        currentpw = request.POST.get('currentPassword', '')
        newpw = ''
        if request.POST.get('newPassword', '') != '' and request.POST.get('newPassword', '') == request.POST.get('confirmPassword', ''):
            newpw = request.POST.get('newPassword', '')

        user = authenticate(username=request.session['username'], password=currentpw)
        
        if user is not None and newpw != '':
            user.set_password(newpw)
            user.save()
    elif request.method == 'POST' and request.POST.get('id') == 'updateAccount':
        print('updating account')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        name = request.POST.get('fname') + ' ' + request.POST.get('lname')

        user = User.objects.get(username=request.session['username'])
        login = LoginModel.LoginModel(email)

        if username != '':
            validateUser = authenticate(request, username=username)
            if validateUser is None:
                user.username = username
                request.session['username'] = username
        if name != ' ':
            user.first_name = request.POST.get('fname')
            user.last_name = request.POST.get('lname')
            request.session['name'] = name

        login.updateUser(name=name)
        user.save()

    return render(request, 'ManageAccount/account.html')