from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm 
from .models import ExtUser, Degree
from django.forms import ModelForm

# form for logging in
# based on inbuilt authentication form
class loginForm(AuthenticationForm):
    pass

# form for creating user accounts
# based on user model
class createAccountForm(ModelForm):
    class Meta:
        model = ExtUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'degree', 'description', 'dob' ]
    #degree = forms.ModelChoiceField(queryset=Degree.objects.all())
# form for editing user profiles
class editAccountForm(forms.Form):
    class Meta:
        model = ExtUser
        fields = ['password', 'email', 'description', 'degree']
    """
    dob = forms.DateField(
        input_formats=['%Y-%m-%d'],
        label='Date of Birth',
        required= True, 
    )
    university = forms.ChoiceField(
        choices = 'dog', 
        help_text="Which university you go to", 
        label='University',
        required= True, 
    )
    degree = forms.ChoiceField(
        choices = 'dog', 
        help_text="Which degree are you studying under?", 
        label='Degree ',
        required= True, 
    )
    email = forms.CharField(
        label='Email',
        required= True, 
    )
    password = forms.CharField(
        help_text="Enter password", 
        label='Password ',
        required= True, 
    )
    description = forms.CharField(
        help_text="Describe yourself", 
        label='Description ',
        required= False, 
    )
    """
    def clean_data(self, data):
        cl_data = self.cleaned_data[data]
        return cl_data


# form for searching textbooks
class textbookSearchForm(forms.Form):
    search = forms.CharField(
        label='Search', 
        required=False,
    )
    degree_filter = forms.ChoiceField(
        choices = 'dog', 
        label='Search by Current Course',
        required=False, 
    )

    def clean_data(self):
        cl_data = self.cleaned_data['username']
        cl_data = self.cleaned_data['password']
        return cl_data

