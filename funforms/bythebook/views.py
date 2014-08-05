from django.views.generic.edit import FormView
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import transaction

from bythebook.models import BookForm, AuthorForm, Author


class BookView(FormView):
    template_name = 'book.html'
    form_class = BookForm
    success_url = '/book-added'

    def form_valid(self, form):
        form.save(self.request, True)
        return super(BookView, self).form_valid(form)


class BookAddedView(TemplateView):
    template_name = 'book-added.html'


class BookManualView(View):
    form_class = BookForm
    template_name = 'manual.html'
    success_url = '/manual'

    def get(self, request):
        book = BookForm()
        authors = []
        for ii in xrange(3):
            authors.append(AuthorForm())

        c = RequestContext(request, {'authors': authors, 'book': book})
        return render_to_response(self.template_name, c)

    @transaction.atomic
    def post(self, request):
        name = request.POST.get('name')
        print name

        authors = request.POST.getlist('author_name')
        titles =  request.POST.getlist('author_title')

        author_models = []
        for ii,author in enumerate(authors):
            author_name = author
            author_title = titles[ii]
            cur = {"author_name": author_name, "author_title": author_title}
            a = AuthorForm(cur)

            if a.is_valid():
                obj = Author.objects.filter(
                    name=author_name, title=author_title)
                if obj:
                    a_model = obj[0]
                else:
                    a_model = a.save(commit=False)
                author_models.append(a_model)
            else:
                print a.errors
            print "---"

        print author_models

        author_ids = []
        for a_model in author_models:
            a_model.save()
            author_ids.append(a_model.id)

        book_form = BookForm({"name": name, "authors": author_ids})
        if book_form.is_valid():
            book_form.save(commit=True)
        else:
            print book_form.errors

        return HttpResponse("Hi")


    def form_valid(self, form):
        print "form valid"
        return super(BookManualView, self).form_valid(form)

    def form_invalid(self, form):
        print "form not valid"
        return super(BookManualView, self).form_valid(form)
