from django import forms 
from .models import auto

class AutoForm(forms.ModelForm):
    class meta:
        model = auto
        exclude = ['timestamp']
        