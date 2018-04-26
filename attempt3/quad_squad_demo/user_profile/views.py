from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from.forms import createAccountForm

def index(request):
    form = createAccountForm(request.POST)
    return render(request, 'user_profile.html', {'form':form}) 

# Create your views here.
