
from django import forms
from .models import Page

class FormModel(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title','content','order']