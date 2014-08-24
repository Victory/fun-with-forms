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
    check_this = forms.BooleanField()

    def clean(self):
        cleaned = self.cleaned_data
        #import pdb; pdb.set_trace()

        if cleaned.get('check_this') and not cleaned.get('might_need_this'):
            self.add_error('might_need_this', 'If checked you need this')
            raise forms.ValidationError(
                "You Checked this but didn't set in a value",
                code="checked_needed")

        return cleaned

    class Meta:
        model = HideyShowy
        fields = ['definitely_need_this', 'might_need_this', 'check_this']

        widgets = {
            'definitely_need_this':
            forms.TextInput(attrs={'cols': 80, 'rows': 20}),
            'might_need_this':
            forms.TextInput(attrs={'cols': 80, 'rows': 20}),

        }
