from django.db import models
from django import forms

TITLE_CHOICES = (('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.'))


class Author(models.Model):
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.name


class AuthorForm(forms.ModelForm):
    def add_prefix(self, field_name):
        return "author_" + field_name
    class Meta:
        model = Author
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'cols': 80, 'rows': 20}),
            'title': forms.Select(attrs={'cols': 80, 'rows': 20})
        }


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'authors']
        widgets = {
            'name': forms.TextInput(attrs={'cols': 80, 'rows': 20}),
        }

    """
    def save(self, request, commit=True):
        instance = super(BookForm, self).save(request)
        instance.save(update_fields=['name'])

        pass
    """
