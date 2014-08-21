from django.db import models
from django import forms

# Create your models here.


class HideyShowy(models.Model):
    definitely_need_this = models.CharField (
        max_length = 200)

    might_need_this = models.CharField(
        max_length=30,
        blank=True)


class HideyShowyForm(forms.ModelForm):
    class Meta:
        model = HideyShowy
        fields = ['definitely_need_this', 'might_need_this']

        widgets = {
            'definitely_need_this':
            forms.TextInput(attrs={'cols': 80, 'rows': 20}),
            'might_need_this':
            forms.Select(attrs={'cols': 80, 'rows': 20})
        }
