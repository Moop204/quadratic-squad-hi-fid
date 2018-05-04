from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .controller import userQueries

@login_required(redirect_field_name='login')
def index(request):
    # HERE BE USER QUERIES
    id = request.user.id
    c_user = userQueries.findUser(id)
    name = c_user.first_name + c_user.last_name
    description = c_user.description + "HI DEREEE" 
    #degree = userQueries.findUserDegree(id)
    print(description)
    if request.method == 'POST' and 'edit' in request.POST:
        return redirect('edit')
    elif request.method == 'POST' and 'meetup' in request.POST:
        return redirect('main_meetup')
    elif request.method == 'POST' and 'match' in request.POST:
        return redirect('match')
    elif request.method == 'POST' and 'message' in request.POST:
        return redirect('main_message')
    elif request.method == 'POST' and 'textbook' in request.POST:
        return redirect('main_textbook')
    return render(request, 'dashboard.html', {'name':name}, {'description':description},)# {'degree':degree})

def main_match(request):
    return render(request, 'match.html',) 

def main_message(request):
    return render(request, 'message.html',) 

def main_meetup(request):
    return render(request, 'meetup.html',) 

def main_textbook(request):
    return render(request, 'textbook.html',) 

def main_profile(request):
    return render(request, 'user_profile.html',) 

