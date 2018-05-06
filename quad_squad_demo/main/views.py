from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .controller import userQueries, loginQueries, matchMaker
from .forms import loginForm, createAccountForm, textbookSearchForm, createAccountForm, editAccountForm
from .models import ExtUser #<<--needed???

from django.contrib import messages

#DASHBOARD
@login_required(redirect_field_name='login')
def index_dashboard(request):
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

# LOGIN

# Create your views here.
def index_login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
    else:
        form = loginForm()
    render( request, 'home.html', {'form':form})
    if request.method == 'POST' and 'form_login' in request.POST:
        return authLogin(request)
    elif request.method == 'POST' and 'form_create' in request.POST:
        form = createAccountForm()
        return redirect('sign_up')
    else:
        form = loginForm()
        return render( request, 'home.html', {'form':form})

def create_account(request):
    if request.method == 'POST':
        form = createAccountForm(request.POST)
    else:
        form = createAccountForm()
    if request.method =='POST' and 'form_create' in request.POST: 
        print("FORM CREATE")
        return redirect('create_account')
    elif 'submit' in request.POST and createAccountForm(request.POST).is_valid(): 
        in_dob = request.POST['dob']
        in_degree = request.POST['degree']
        in_email = request.POST['email']
        in_description = request.POST['description']
        in_password = request.POST['password']
        in_first_name = request.POST['first_name']
        in_last_name = request.POST['last_name']
        in_username = request.POST['username']
        userQueries.addUser(in_dob, in_degree, in_email, in_description, in_password, in_username, in_first_name, in_last_name)
        return redirect('dashboard')
    return render(request, 'create_account.html', {'form':form})

# possibly move to controller
def authLogin(request):
    in_username = request.POST['username']
    in_password = request.POST['password']
    user = authenticate(request, username=in_username, password=in_password)
    if user is not None:
        login(request, user) 
        return redirect('dashboard')
    else:
        return redirect('login')

#match

def index_match(request):
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

#meetups
from django.shortcuts import render

def index_meetup(request):
    return render(request, 'meetup.html',) 

# Create your views here.

#message
from django.shortcuts import render

def index_message(request):
    return render(request, 'message.html',) 

# Create your views here.

#textbook
def index_textbook(request):
    if request.method == 'POST':
        form = textbookSearchForm(request.POST)
    else:
        form = textbookSearchForm()
    return render(request, 'textbook.html', {'form':form}) 

def textbook_detailed(request):
    return render(request, 'textbook_individual.html') 
    
#user profile

def index_user_profile(request):
    if request.method == 'POST':
        form = editAccountForm(request.POST)
    else:
        form = editAccountForm()
    return render(request, 'user_profile.html', {'form': form}, {'bus': 'DAWG'}, ) 

def specific_index(request, user_id):
    user = User.objects.filter(id=user_id).first() # bad style, move this into controller later
    return render(request, 'specific_profile.html', {'user': user}, ) 

