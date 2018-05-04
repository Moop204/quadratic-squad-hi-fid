from django.shortcuts import render
from django.contrib import messages
from . controller import matchMaker
from user_profile.models import ExtUser 

def index(request):
    id = request.user.id
    matchedList = matchMaker.findMatches(id)
    #receivedList = matchMaker.getRequestList(id)
    print(matchedList)
    if request.method == "POST" and 'find' in request.POST:  
        return redirect('/find/') 
    else:
        messages.info(request, 'Find your match') 
    return render(request, 'match.html', {'matched_list':matchedList}, )#{'received_list':receivedList}) 
        

# Create your views here.
