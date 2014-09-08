from django.db import models
from django import forms


class Pretty(models.Model):
    name = models.CharField (
        max_length = 200)


class PrettyForm(forms.ModelForm):

    class Meta:
        model = Pretty
        fields = ['name']
    pass
