from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import loginForm
from .controller import *
from user_profile.forms import createAccountForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
    else:
        form = loginForm()
    return render( request, 'home.html', {'form':form})

def create_account(request):
    if request.method == 'POST':
        form = createAccountForm(request.POST)
    else:
        form = createAccountForm()
    render( request, 'create_account.html', {'form':form})
    return redirect('credentials')

def login(request):
    if request.method == 'POST':
        in_username = request.POST['username']
        in_password = request.POST['password']
        if loginQueries.loginValidation(in_username, in_password) == True:
            user_id = loginQueries.loginID(in_username, in_password)
            render(request, 'create_account.html',)
            return redirect('dashboard')
    return redirect('submit_credentials')
