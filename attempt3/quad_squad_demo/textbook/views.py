from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'textbook.html',) 

def textbook_detailed(request):
    return render(request, 'textbook_individual.html',) 
    
# Create your views here.
