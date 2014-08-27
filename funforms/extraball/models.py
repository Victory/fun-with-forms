from django.db import models
from django import forms

# Create your models here.

class ExtraBallForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    source = forms.CharField(max_length=100)


class ExtraBallForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


class ExtraBallForm3(forms.Form):
    token = forms.CharField(widget=forms.Textarea)
