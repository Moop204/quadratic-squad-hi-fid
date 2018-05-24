from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
from django.forms import ModelForm, ModelChoiceField

# form for creating user accounts
# based on user model
class CreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ExtUser
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'description', 'dob' ]

# form for editing users
# based on user model
class AccountForm(ModelForm):
    class Meta:
        model = ExtUser
        fields = ['description']

# form for enrolments
class EnrolmentForm(ModelForm):
    class Meta:
        model = Enrolment
        fields = ['course']

class MessageForm(forms.Form):
    message = forms.CharField(label='Message: ', required = False)

'''
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
'''
