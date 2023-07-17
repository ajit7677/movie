from django.core import validators
from django import forms
from .models import movies01

class rating(forms.ModelForm):
    # dropdown_choices = (
    #     ('option1', '1')
    #     ('option1', '2')
    #     ('option1', '3')
    #     ('option1', '4')
    #     ('option1', '5')
    # )
    class Meta:
        model = movies01
        fields = ['Title', 'Rate']