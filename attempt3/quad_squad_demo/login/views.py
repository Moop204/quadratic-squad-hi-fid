from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect 
from .forms import loginForm, createAccountForm, ExtUser
#from user_profile.forms import createAccountForm
from .controller import loginQueries, userQueries
#from user_profile.models import *
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
    else:
        form = loginForm()
    render( request, 'home.html', {'form':form})
    if request.method == 'POST' and 'form_login' in request.POST:
        return authLogin(request)
    elif request.method == 'POST' and 'form_create' in request.POST:
        form = createAccountForm()
        render( request, 'create_account.html', {'form':form})
        print("~~~!!!~~~")
        return create_account(request)
    else:
        form = loginForm()
        return render( request, 'home.html', {'form':form})

def create_account(request):
    if request.method == 'POST':
        form = createAccountForm(request.POST)
    else:
        form = createAccountForm()
    if request.method =='POST' and 'form_create' in request.POST: 
        print("FORM CREATE")
        return redirect('create_account')
    elif 'submit' in request.POST and createAccountForm(request.POST).is_valid(): 
        in_dob = request.POST['dob']
        in_degree = request.POST['degree']
        in_email = request.POST['email']
        in_description = request.POST['description']
        in_password = request.POST['password']
        in_first_name = request.POST['first_name']
        in_last_name = request.POST['last_name']
        in_username = request.POST['username']
        userQueries.addUser(in_dob, in_degree, in_email, in_description, in_password, in_username, in_first_name, in_last_name)
        return redirect('dashboard')
    return render( request, 'create_account.html', {'form':form})

# possibly move to controller
def authLogin(request):
    in_username = request.POST['username']
    in_password = request.POST['password']
    user = authenticate(request, username=in_username, password=in_password)
    if user is not None:
        login(request, user) 
        return redirect('dashboard')
    else:
        return redirect('login')


