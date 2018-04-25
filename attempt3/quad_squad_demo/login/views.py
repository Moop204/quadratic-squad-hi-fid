from django.shortcuts import render
from django.http import HttpResponseRedirect
from.forms import loginForm
# Create your views here.
def index(request):
    form = loginForm(request.POST)
    return render( request, 'home.html', {'form':form})

def create_account(request):
    #if request.POST.get("create","")
    return render( request, 'create_account.html',)
    
def submit_credentials(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid() and 'form_login' in request.POST:
            username = form.clean_data['username']
            password = form.clean_data['password']
            redirect(request, 'dashboard')

    else:
        HttpResponseRedirect(reverse('create_account/') )
        return redirect( request, 'credentials',)

"""
    View function for home page of site.
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )
"""
    
