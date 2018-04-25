from django.shortcuts import render
from django.http import HttpResponseRedirect
from.forms import loginForm
# Create your views here.
def index(request):
    form = loginForm(request.POST)
    return render( request, 'home.html', {'form':form})

def create_account(request):
    return render( request, 'create_account.html',)
    
def login(request):
    return render( request, 'create_account.html',)


