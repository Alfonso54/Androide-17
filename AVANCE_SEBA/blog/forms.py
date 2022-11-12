from django import forms 
from .models import Auto

class AutoForm(forms.ModelForm):
    class meta:
        model = Auto
        exclude = ['timestamp']