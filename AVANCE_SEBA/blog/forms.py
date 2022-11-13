from django import forms 
from .models import BlogsPost

class AutoForm(forms.ModelForm):
    class meta:
        model = BlogsPost
        exclude = ['timestamp']