from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class loginForm(forms.Form):
    username = forms.CharField(help_text="Enter username", label='Username', required=False,)
    password = forms.CharField(help_text="Enter password", label='Password ', required=False,)

    def clean_data(self):
        cl_data = self.cleaned_data['username']
        cl_data = self.cleaned_data['password']
        return cl_data

class createAccountForm(forms.Form):
    preferredName = forms.CharField(help_text="Enter Preferred", label='Preferred Name',)
    fullName = forms.CharField(help_text="Enter Full Name", label='Full Name ',)
    username = forms.CharField(help_text="Enter username", label='Username',)
    password = forms.CharField(help_text="Enter password", label='Password ',)
    
    def clean_data(self):
        cl_data = self.cleaned_data['username']
        cl_data = self.cleaned_data['password']
        cl_data = self.cleaned_data['preferredName']
        cl_data = self.cleaned_data['fullName']
        return cl_data                
