from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class createAccountForm(forms.Form):
    preferredName = forms.CharField(help_text="Enter Preferred", label='Preferred Name',)
    fullName = forms.CharField(help_text="Enter Full Name", label='Full Name ',)
    username = forms.CharField(help_text="Enter username", label='Username',)
    password = forms.CharField(help_text="Enter password", label='Password ',)
    
    def clean_data(self, data):
        cl_data = self.cleaned_data[data]
        return cl_data

        
