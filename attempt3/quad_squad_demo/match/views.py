from django.shortcuts import render
from django.contrib import messages

def index(request):
    if request.method == "POST":  
        return render(request, 'match.html',) 
    else:
        message.info(request, 'Find your match') 
        return redirect('/find/') 
        

# Create your views here.
