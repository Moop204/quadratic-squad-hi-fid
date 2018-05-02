from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from quad_squad_demo.choices import *
 
class textbookSearchForm(forms.Form):
    search = forms.CharField(
        label='Search', 
        required=False,
    )
    degree_filter = forms.ChoiceField(
        choices = LIST_DEGREES, 
        label='Search by Current Course',
        required=False, 
    )

    def clean_data(self):
        cl_data = self.cleaned_data['username']
        cl_data = self.cleaned_data['password']
        return cl_data

