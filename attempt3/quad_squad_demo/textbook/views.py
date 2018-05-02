from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *

def index(request):
    if request.method == 'POST':
        form = textbookSearchForm(request.POST)
    else:
        form = textbookSearchForm()
    return render(request, 'textbook.html', {'form':form}) 

def textbook_detailed(request):
    return render(request, 'textbook_individual.html') 
    
# Create your views here.
