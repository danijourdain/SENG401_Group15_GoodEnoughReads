from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from gersiteapp import LoginModel

# logout the user, then redirect to the login page
def logout_view(request):
    auth.logout(request)
    return redirect('login')

# validate user credentials then create a new account
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        uname = request.POST.get('username', '')
        pw1 = request.POST.get('password', '')
        pw2 = request.POST.get('password2', '')
        username = None
        user = None
        # get all the fields from the form

        try:
            username = User.objects.get(username=uname)
            user = User.objects.get(email=email)
        except:
            pass

        login = LoginModel.LoginModel(email)
        uniqueEmail = login.verifyUser()
        if not uniqueEmail:
            error_message = "That email is already signed up!"
            # template currently not made
            return render(request, 'ManageAccount/signup.html', {'error_message': error_message})
        elif username is not None:
            error_message = "That username is already signed up!"
            # template currently not made
            return render(request, 'ManageAccount/signup.html', {'error_message': error_message})


        if user is None and pw1 == pw2:
            user = User.objects.create_user(username=uname, password=pw1, email=email)
            user.first_name = fname
            user.last_name = lname
            user.save()
            login.signupUser()
            # create the user and save their information to the database
            
            request.session['username'] = uname
            request.session['name'] = fname + " " + lname
            request.session['email'] = email
            return redirect('welcome')
            # if the signup is successful, set the session variables thne go to the homepage
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
        # get the information from the html form

        try:
            user = User.objects.get(username=uname)
        except:
            error_message = "Invalid username"
            return render(request, 'ManageAccount/reset_password.html', {'error_message': error_message})
        # check if there is a user with the username

        if user is not None and user.email == email and pw1 == pw2 and pw1 != '':
            user.set_password(pw1)
            user.save()

            request.session['username'] = uname
            request.session['name'] = user.first_name + " " + user.last_name
            request.session['email'] = user.email
            return redirect('welcome')
            # if the credentials are valid, set the session variables and redirect to the welcome page
        else:
            error_message = "Invalid email"
            return render(request, 'ManageAccount/reset_password.html', {'error_message': error_message})
            # otherwise return an error message
    else:
        return render(request, 'ManageAccount/reset_password.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:    #there is an existing user with these credentials
            request.session['username'] = username
            request.session['name'] = user.first_name + " " + user.last_name
            request.session['email'] = user.email
            
            return redirect('welcome')  
            # set the session variables and then go to the homepage
        else:
            error_message = "Invalid login credentials"
            return render(request, 'ManageAccount/registration/login.html', {'error_message': error_message})
            # otherwise return an error message
    else:
        return render(request, 'ManageAccount/registration/login.html')

def account(request):
    if request.method == 'POST' and request.POST.get('id') == 'updatePassword':
        currentpw = request.POST.get('currentPassword', '')
        newpw = ''
        if request.POST.get('newPassword', '') != '' and request.POST.get('newPassword', '') == request.POST.get('confirmPassword', ''):
            newpw = request.POST.get('newPassword', '')
            # check if the passwords match and are not empty

        user = authenticate(username=request.session['username'], password=currentpw)
        # get the existing user with the existing password
        
        if user is not None and newpw != '':
            user.set_password(newpw)
            user.save()
            # update password for the user
    elif request.method == 'POST' and request.POST.get('id') == 'updateAccount':
        print('updating account')
        username = request.POST.get('username', '')
        fname = request.POST.get('fname', '') 
        lname = request.POST.get('lname', '')
        # get the information from the html form

        user = User.objects.get(username=request.session['username'])
        login = LoginModel.LoginModel(request.session['email'])

        if username != '':
            try:
                User.objects.get(username=username)
                error_message = "Username is already taken!"
                return render(request, 'ManageAccount/account.html', {'error_message': error_message})
                # check if the new username is available
            except:
                user.username = username
                request.session['username'] = username
                # if the username is free, update the user
        if fname != '' and lname != '':
            user.first_name = request.POST.get('fname')
            user.last_name = request.POST.get('lname')
            request.session['name'] = fname + ' ' + lname
            login.updateUser(name=(fname + ' ' + lname))
            # update the name if it is filled in

        user.save()
        # save any changes to the user

    return render(request, 'ManageAccount/account.html')