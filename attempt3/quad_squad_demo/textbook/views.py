from django.shortcuts import render

def index(request):
    return render(request, 'textbook.html',) 

# Create your views here.
