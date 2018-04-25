from django.shortcuts import render

def index(request):
    return render(request, 'match.html',) 

# Create your views here.
