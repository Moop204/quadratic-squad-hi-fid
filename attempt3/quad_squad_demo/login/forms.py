from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class loginForm(forms.Form):
    username = forms.CharField(help_text="Enter username", label='Username', required=True,)
    password = forms.CharField(help_text="Enter password", label='Password ', required=True,)

    def clean_data(self):
        cl_data = self.cleaned_data['username']
        cl_data = self.cleaned_data['password']
        return cl_data


