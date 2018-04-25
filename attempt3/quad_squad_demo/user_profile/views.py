from django.shortcuts import render

def index(request):
    return render(request, 'edit.html',) 

# Create your views here.
