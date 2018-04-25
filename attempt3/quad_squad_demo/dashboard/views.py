from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.shortcuts import render

def index(request):
    return render(request, 'dashboard.html',)

def main_match(request):
    return render(request, 'match.html',) 

def main_message(request):
    return render(request, 'message.html',) 

def main_meetup(request):
    return render(request, 'meetup.html',) 

def main_textbook(request):
    return render(request, 'textbook.html',) 

def main_profile(request):
    return render(request, 'edit.html',) 

