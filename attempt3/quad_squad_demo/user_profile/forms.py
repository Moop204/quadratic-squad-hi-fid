from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from quad_squad_demo.choices import *
from django.forms.widgets import *

class editAccountForm(forms.Form):
    preferredName = forms.CharField(
        help_text="Enter Preferred", 
        label='Preferred Name',
        label_suffix='',
        required= True, 
    )
    birthday = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format = '%d/%m/%Y'),
        label='Date of Birth',
        required= True, 
    )
    university = forms.ChoiceField(
        choices = LIST_UNIVERSITIES, 
        help_text="Which university you go to", 
        label='University ',
        required= True, 
    )
    degree = forms.ChoiceField(
        choices = LIST_DEGREES, 
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
    
    def clean_data(self, data):
        cl_data = self.cleaned_data[data]
        return cl_data

class createAccountForm(editAccountForm):
    fullName = forms.CharField(
        help_text="Enter Full Name", 
        label='Full Name ',
        label_suffix='',
        required= True, 
    )
    username = forms.CharField(
        help_text="Enter username", 
        label='Username',
        required= True, 
    )

        
