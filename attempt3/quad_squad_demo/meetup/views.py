from django.shortcuts import render

def index(request):
    return render(request, 'meetup.html',) 

# Create your views here.
