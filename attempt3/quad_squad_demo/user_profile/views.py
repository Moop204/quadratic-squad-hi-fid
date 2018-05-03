from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import createAccountForm, editAccountForm

from user_profile.models import User # bad style, move this into controller later

def index(request):
    if request.method == 'POST':
        form = editAccountForm(request.POST)
    else:
        form = editAccountForm()
    return render(request, 'user_profile.html', {'form': form}, {'bus': 'DAWG'}, ) 

def specific_index(request, user_id):
    user = User.objects.filter(id=user_id).first() # bad style, move this into controller later
    return render(request, 'specific_profile.html', {'user': user}, ) 

# Create your views here.
