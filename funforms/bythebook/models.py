from django.db import models
from django import forms

from bythebook.validators import title_does_not_start_with_quote

TITLE_CHOICES = (('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.'))


class Author(models.Model):
    title = models.CharField(
        max_length=3,
        choices=TITLE_CHOICES)
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[title_does_not_start_with_quote])
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=200)
    book = models.ForeignKey(Book, blank=True)

    def __unicode__(self):
        return self.name

class TopicForm(forms.ModelForm):
    def add_prefix(self, field_name):
        return "topic_" + field_name

    class Meta:
        model = Topic
        fields = ['name', 'book']
        widgets = {
            'name': forms.TextInput(attrs={'cols': 80, 'rows': 20})
        }


class AuthorForm(forms.ModelForm):
    def add_prefix(self, field_name):
        return "author_" + field_name

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)

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
