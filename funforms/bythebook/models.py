from django.db import models
from django.forms import ModelForm, Textarea

# Create your models here.

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.')
)


class Author(models.Model):
    name = models.CharField(max_length=80)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.name


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def save(self, request, commit=True):
        super(BookForm, self).save(request)
        pass
