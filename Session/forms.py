from django import forms
from .models import Session
class SessionForms(forms.ModelForm):
    class Meta:
        model=Session
        fields='__all__'


