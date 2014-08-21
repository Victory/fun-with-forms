from django.db import models
from django import forms

# Create your models here.


class HideyShowy(models.Model):
    definitely_need_this = models.CharField (
        max_length = 200)

    might_need_this = models.CharField(
        max_length=30,
        blank=True)


class HideyShowyForm():
    class Meta:
        model = HideyShowy
