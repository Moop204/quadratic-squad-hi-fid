from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
from django.forms import ModelForm, ModelChoiceField, Textarea

# form for creating user accounts
# based on user model
class CreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ExtUser
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'description', 'dob' ]
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

# form for editing users
# based on user model
class AccountForm(ModelForm):
    class Meta:
        model = ExtUser
        fields = ['description']
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 10}),
        }


# form for enrolments
class EnrolmentForm(ModelForm):
    class Meta:
        model = Enrolment
        fields = ['course']

class MessageForm(forms.Form):
    message = forms.CharField(label='Message', required = False)

class MeetupForm(ModelForm):
    class Meta:
        model = Pending_Meetup
        fields = ['guest', 'location', 'time', 'date', 'description']
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 10}),
        }
    
# form for searching textbooks
class TextbookSearchForm(forms.Form):
    search = forms.CharField(
        label='Search', 
        required=False,
    )


