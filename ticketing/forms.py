from django import forms
from .models import Event

class PostForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('image', 'body')