from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import createAccountForm, editAccountForm

def index(request):
    if request.method == 'POST':
        form = editAccountForm(request.POST)
    else:
        form = editAccountForm()
    return render(request, 'user_profile.html', {'form': form}, {'bus': 'DAWG'}, ) 

def specific_index(request, user_id):
    return render(request, 'specific_profile.html', {'user_id': user_id}, ) 

# Create your views here.
