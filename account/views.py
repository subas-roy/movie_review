from django.shortcuts import redirect, render
from account.forms import SignupForm, SignInForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form' : SignupForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {'form' : SignupForm(), 'error' : "An account already exists with this username"})       
        else:
            return render(request, 'signup.html', {'form' : SignupForm(), 'error' : "Password didn't match"})


def signIn(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form' : SignInForm()})
    else:
        user = authenticate(username=request.POST['username'], 
                            password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'form' : SignInForm(), 'error' : "Username and password doesn't match"})       
        else:
            login(request, user)
            return redirect('home')
        

def logoutAccount(request):
    logout(request)
    return redirect('home')