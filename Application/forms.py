from django import forms
from .models import Application
class ApplicationForms(forms.ModelForm):
    class Meta:
        model=Application
        fields='__all__'


