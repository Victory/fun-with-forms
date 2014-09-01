from django.db import models
from django import forms

from extraball.validators import validate_subject
# Create your models here.

class ExtraBallForm1(forms.Form):
    subject = forms.CharField(
        max_length=100,
        validators=[validate_subject])

    source = forms.CharField(max_length=100)


class ExtraBallForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


class ExtraBallForm3(forms.Form):
    token = forms.CharField(widget=forms.Textarea)
