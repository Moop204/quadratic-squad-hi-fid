from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm 
from user_profile.models import ExtUser
from django.forms import ModelForm
  
class loginForm(AuthenticationForm):
    pass
    #username = forms.CharField(help_text="Enter username", label='Username', required=True,)
    #password = forms.CharField(help_text="Enter password", label='Password ', required=True,)

class createAccountForm(ModelForm):
    class Meta:
        model = ExtUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'degree', 'description', 'dob' ]
