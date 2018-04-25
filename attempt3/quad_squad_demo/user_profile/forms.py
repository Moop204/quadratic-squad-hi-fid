from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class loginForm(forms.Form):
    username = forms.CharField(help_text="Enter username", label='Username', required=False,)
    password = forms.CharField(help_text="Enter password", label='Password ', required=False,)
    
    def clean_data(self, data):
        cl_data = self.cleaned_data[data]
        return cl_data

        
