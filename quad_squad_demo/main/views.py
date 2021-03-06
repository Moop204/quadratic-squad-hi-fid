from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, get_user, logout
from .controller import *
from django.contrib.auth.forms import AuthenticationForm 
from .forms import *
from .models import *
from django.contrib import messages
from django.forms import modelformset_factory, formset_factory

@login_required(redirect_field_name='login')
def index_dashboard(request):
    user = get_user(request)
    enrolments = []
    for enrolment in Enrolment.objects.filter(user=user).all():
        enrolments.append(enrolment.course)
    return render(
        request, 
        'dashboard.html', 
        {
            'name':user.first_name, 
            'description':user.description, 
            'enrolments':enrolments
        }
    )
#base login page
def index_login(request):
    # build form
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
    else:
        form = AuthenticationForm()
        return render(
            request, 
            'home.html', 
            {
                'form':form
            }
        )
    #login was chosen, authenticate credentials
    if 'form_login' in request.POST and form.is_valid():
        in_username = form.cleaned_data['username']
        in_password = form.cleaned_data['password']
        user = authenticate(
            request, 
            username=in_username, 
            password=in_password
        )
        if user is not None:
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
    EnrolmentFormSet = modelformset_factory(Enrolment, fields=('course',), extra=4)
    if (request.method == "POST"):
        form = CreateForm(request.POST)
        form2 = EnrolmentFormSet(request.POST, request.FILES)
    else:
        form = CreateForm()
        form2 = EnrolmentFormSet(queryset=Enrolment.objects.none())
        return render(
            request,
            'create_account.html', 
            {
                'form':form, 
                'enrolments':form2,
            }
        )

    # submit account details, redirect to dashboard
    if (form.is_valid() and form2.is_valid()):
        if 'create' in request.POST:
            user = form.save()
            for f in form2:
                if ('course' in f.cleaned_data):
                    enrolment = Enrolment(user=user, course=f.cleaned_data['course'])
                    enrolment.save()
            login(request, user)
            return redirect('dashboard')
    else:
            return render(
                request, 
                'create_account.html', 
                {
                    'form':form, 
                    'enrolments':form2,
                }
            )

    # some kinda error if it ever gets to here
    return redirect('login')

@login_required(redirect_field_name='login')
def index_logout(request):
    logout(request)
    return redirect('login')

# editing profile page
@login_required(redirect_field_name='login')
def edit_profile(request):
    # build forms
    EnrolmentFormSet = modelformset_factory(Enrolment, fields=('course',), extra=4, can_delete=True)
    user = get_user(request)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=user)
        form2 = EnrolmentFormSet(request.POST, request.FILES)
        if (form.is_valid() and form2.is_valid()):
            form.save()
            # formset data has to be saved separately
            new_instances = form2.save(commit=False)
            for f in form2.deleted_objects:
                f.delete()
            for new_instance in new_instances:
                new_instance.user = user
                try:
                    new_instance.save()
                except:
                    pass

            return redirect('dashboard')
        else:
            return render(
                request,
                'user_profile.html', 
                {
                    'form':form, 
                    'form2':form2,
                }
            )
    else:
        form = AccountForm(instance=user)
        form2 = EnrolmentFormSet(queryset=Enrolment.objects.filter(user=user).all())
        return render(
            request, 
            'user_profile.html',
            {
                'form':form,
                'form2':form2,
            }
        )
    # some kinda error if it ever gets to here
    return redirect('login')

# viewing other user's page
@login_required(redirect_field_name='login')
def specific_user(request, user_id):
    specific = ExtUser.objects.filter(id=user_id).first()
    if (request.method == "POST"):
        user = get_user(request)
        if (specific != user):
            otherWay = Matches.objects.filter(receiver=user).filter(sender=specific).first()
            if (otherWay is not None):
                if (otherWay.status == 'a'):
                    # match already exists the other way, do nothing
                    pass
                else:
                    # there is a match request the other way, accept it
                    otherWay.status = 'a'
                    otherWay.save()
            else:
                match = Matches(sender=user, receiver=specific, status='p')
                try:
                    match.save()
                except:
                    pass
        return redirect('match')
    return render(request, 'specific_profile.html', {'user':specific})

# main match page
@login_required(redirect_field_name='login')
def index_match(request):
    user = get_user(request)
    received_requests = []
    sent_requests = []
    matched_list = []
    search_results = []

    # get match results
    for received in Matches.objects.filter(status='p').filter(receiver=user).all():
        received_requests.append(received.sender)
    for sent in Matches.objects.filter(status='p').filter(sender=user).all():
        sent_requests.append(sent.receiver)
    for match in Matches.objects.filter(status='a').filter(sender=user).all():
        matched_list.append(match.receiver)
    for match in Matches.objects.filter(status='a').filter(receiver=user).all():
        matched_list.append(match.sender)

    # get search results
    if (request.method == "POST"):
        form = EnrolmentForm(data=request.POST)
        if (form.is_valid()):
            course = form.cleaned_data['course']
            for enrol in Enrolment.objects.filter(course=course).exclude(user=user).all():
                if (enrol.user in received_requests + sent_requests + matched_list + search_results):
                    pass
                else:
                    search_results.append(enrol.user)
    else:
        form = EnrolmentForm()

    return render(request, 'match.html', {'received_requests':received_requests, 'sent_requests':sent_requests, 'matched_list':matched_list, 'form':form, 'search_results':search_results})

# main meetup page
@login_required(redirect_field_name='login')
def index_meetup(request):
    user = get_user(request)
    if (request.method == "POST"):
        form = MeetupForm(request.POST)
        # make new meetup
        if (form.is_valid() and "request" in request.POST):
            data = form.cleaned_data
            if (user is not data['guest']):
                new_meetup = Pending_Meetup(host=user, guest=data['guest'], 
                            location=data['location'], time=data['time'], date=data['date'], description=data['description'], status='p')
                try:
                    new_meetup.save()
                    return redirect('meetup')
                except:
                    pass
        else:
            form = MeetupForm()
        # accept meetup
        if ("accept" in request.POST):
            accepted_meetup = Pending_Meetup.objects.filter(id=request.POST['accept']).first()
            accepted_meetup.status = 'a'
            try:
                accepted_meetup.save()
            except:
                pass

        # reject meetup
        if ("reject" in request.POST):
            rejected_meetup = Pending_Meetup.objects.filter(id=request.POST['reject']).first()
            try:
                rejected_meetup.delete()
            except:
                pass            
    else:
        form = MeetupForm()

    requests = MeetupQueries.getRequestList(user)
    sends = MeetupQueries.getSentList(user)
    meetups = MeetupQueries.getMeetupList(user)
    matches = []
    for match in Matches.objects.filter(status='a').filter(sender=user).all():
        matches.append(match.receiver)
    for match in Matches.objects.filter(status='a').filter(receiver=user).all():
        matches.append(match.sender)

    return render(request, 'meetup.html',
        {
        'requests':requests,
        'sends':sends,
        'meetups':meetups,
        'form':form,
        'users':matches
        }
    ) 

# main message page
@login_required(redirect_field_name='login')
def index_message(request):
    if (request.method == "POST"):
        form = MessageForm(request.POST)
    else:
        form = MessageForm()

    message = [["Alex", [[1, "Hey you looked like you needed help with AI"], [1, "I'm free all week to help you out if you're up for it"],]], ]
    user = get_user(request).first_name;
    if request.method == 'POST' and 'message' in request.POST and form.is_valid():
        new_message=form.cleaned_data['message']
        message[0][1].append([0, new_message], )

    return render(request, 'message.html',
        {
        'message': message,
        'user': user,
        'form':form,    
        }
    )   

# main textbook page
def index_textbook(request):
    if request.method == 'POST':
        form = TextbookSearchForm(request.POST)
    else:
        form = TextbookSearchForm()
    results=[]
    if request.method == 'POST' and 'search' in request.POST and form.is_valid():
        query = form.cleaned_data['search']
        results = [ ['Artificial Intelligence: a Modern Approach, 4th Ed.', 'Stuart Russell and Peter Norvig', 'Prentice Hall', '2009'], ['Prolog Programming for Artificial Intelligence, 4th Ed.', 'Ivan Bratko', 'Pearson', '2013'], ['Artificial Intelligence: a New Synthesis', 'Nils J. Nilsson', 'Morgan Kaufmann', '1998'], ['Vehicles: Experiments in Synthetic Psychology', 'Valentino Braitenberg', 'MIT Press', '1984'],]
    return render(request, 'textbook.html', 
        {
            'form':form,
            'results':results,
        }
    ) 
