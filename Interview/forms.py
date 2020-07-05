from django import forms
from .models import Interview
class InterviewForms(forms.ModelForm):
    class Meta:
        model=Interview
        fields='__all__'


