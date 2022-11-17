from django.forms import ModelForm
from .models import comentario

class CommentForm(ModelForm):
    class Meta:
        model = comentario
        fields = ('nombre','email','contenido','active')