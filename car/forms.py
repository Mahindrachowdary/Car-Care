from django import forms
from . import models

class signup_form(forms.ModelForm):
    class Meta:
        model=models.Members
        fields=['username','password']
    