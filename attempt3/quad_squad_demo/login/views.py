from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import loginForm
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
    return render( request, 'create_account.html', {'form':form})
    
def login(request):
    return render( request, 'create_account.html',)


