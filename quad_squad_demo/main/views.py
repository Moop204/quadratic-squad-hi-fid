from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .controller import userQueries, loginQueries, matchMaker
from django.contrib.auth.forms import AuthenticationForm 
from .forms import *
from .models import *
from django.contrib import messages

@login_required(redirect_field_name='login')
def index_dashboard(request):
    user = request.user
    if request.method == 'POST' and 'edit' in request.POST:
        return redirect('edit')
    elif request.method == 'POST' and 'meetup' in request.POST:
        return redirect('meetup')
    elif request.method == 'POST' and 'match' in request.POST:
        return redirect('match')
    elif request.method == 'POST' and 'message' in request.POST:
        return redirect('message')
    elif request.method == 'POST' and 'textbook' in request.POST:
        return redirect('textbook')
    return render(request, 'dashboard.html', {'name':user.first_name}, {'description':user.description},)

#base login page
def index_login(request):
    # build form
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
    else:
        form = AuthenticationForm()
        return render(request, 'home.html', {'form':form})
 
    #login was chosen, authenticate credentials
    if 'form_login' in request.POST and form.is_valid():
        in_username = form.cleaned_data['username']
        in_password = form.cleaned_data['password']
        print(in_username)
        print(in_password)
        user = authenticate(request, username=in_username, password=in_password)
        if user is not None:
            print(in_username)
            print(in_password)
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')

    # create account was chosen, redirect to page  
    elif 'form_create' in request.POST:
        return redirect('sign_up')

    # some kinda error if it ever gets to here
    return redirect('login')

# create account page
def create_account(request):
    # build form 
    if request.method == 'POST':
        form = CreateForm(request.POST)
    else:
        form = CreateForm()
        return render(request, 'create_account.html', {'form':form})

    # submit account details, redirect to dashboard  
    if 'create' in request.POST:
        print(form.data)
        if (form.is_valid()):
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'create_account.html', {'form':form})

    # some kinda error if it ever gets to here
    return redirect('login')

# main match page
def index_match(request):
    id = request.user.id
    matchedList = matchMaker.findMatches(id)
    receivedList = matchMaker.getRequestList(id) # currently bugged
    print("matchedList")
    print(matchedList)
    if request.method == "POST" and 'find' in request.POST:  
        return redirect('find') 
    elif request.method == "POST" and 'return' in request.POST:  
        return redirect('dashboard') 
    else:
        messages.info(request, 'Find your match') 
    return render(request, 'match.html', {'matched_list':matchedList}, {'received_list':receivedList}) 
        
from django.shortcuts import render

# main meetup page
def index_meetup(request):
    return render(request, 'meetup.html',) 

# main message page
def index_message(request):
    return render(request, 'message.html',) 

# main textbook page
def match_find(request):
    if request.method == 'POST' and 'return' in request.POST:
        return redirect('return_match')
    return render(request, 'find_match.html',) 
    

# main textbook page
def index_textbook(request):
    if request.method == 'POST':
        form = textbookSearchForm(request.POST)
    else:
        form = textbookSearchForm()
    return render(request, 'textbook.html', {'form':form}) 

# specific textbook page
def textbook_detailed(request):
    return render(request, 'textbook_individual.html') 
    
# editing profile page
def index_user_profile(request):
    if request.method == 'POST':
        form = editAccountForm(request.POST)
    else:
        form = editAccountForm()

    if request.method == 'POST' and 'return' in request.POST:
        return redirect('rreturn_dashboard')
    elif request.method == 'POST' and 'save' in request.POST:
        if editAccountForm(request.POST).is_valid():
            return redirect('rreturn_dashboard')

    elif request.method == 'POST' and 'discard' in request.POST:
        return redirect('rreturn_dashboard')
    #print(form)
    return render(request, 'user_profile.html', {'form': form},) 

# viewing other user's page
def specific_user(request, user_id):
    user = User.objects.filter(id=user_id).first() # bad style, move this into controller later
    return render(request, 'specific_profile.html', {'user': user}, ) 

