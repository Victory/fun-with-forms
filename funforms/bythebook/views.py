from django.views.generic.edit import FormView
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import transaction

from bythebook.models import BookForm, AuthorForm, TopicForm, Author


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
        topic = TopicForm()
        authors = []
        for ii in xrange(3):
            authors.append(AuthorForm())

        c = RequestContext(
            request,
            {'authors': authors,
             'author_prototype': AuthorForm(),
             'book': book,
             'topic': topic})
        return render_to_response(self.template_name, c)

    @transaction.atomic
    def post(self, request):
        name = request.POST.get('name')

        authors = request.POST.getlist('author_name')
        titles = request.POST.getlist('author_title')
        topic_name = request.POST.get('topic_name')

        found_errors = False
        author_models = []
        author_forms = []
        for ii, author in enumerate(authors):
            author_name = author
            author_title = titles[ii]
            if author_name == "" and author_title == "":
                continue

            cur = {"author_name": author_name, "author_title": author_title}
            a = AuthorForm(cur)
            author_forms.append(a)
            if a.is_valid():
                obj = Author.objects.filter(
                    name=author_name, title=author_title)
                if obj:
                    a_model = obj[0]
                else:
                    a_model = a.save(commit=False)
                author_models.append(a_model)
            else:
                found_errors = True

        author_ids = []
        for a_model in author_models:
            a_model.save()
            author_ids.append(a_model.id)

        book_form = BookForm({"name": name, "authors": author_ids})
        book_model = None
        if book_form.is_valid():
            book_model = book_form.save(commit=True)
        else:
            found_errors = True

        if book_model:
            topic_form = TopicForm(
                {"topic_name": topic_name, "topic_book": book_model.id})
            if topic_form.is_valid():
                topic_form.save()
            else:
                found_errors = True
        else:
            topic_form = TopicForm(
                {"topic_name": topic_name, "topic_book": -1})
            topic_form.is_valid()

        if found_errors:
            c = RequestContext(
                request,
                {'authors': author_forms,
                 'book': book_form,
                 'topic': topic_form,
                 'author_prototype': AuthorForm()
                 })
            return render_to_response(self.template_name, c)

        return HttpResponse("Book Added!")

    def form_valid(self, form):
        print "form valid"
        return super(BookManualView, self).form_valid(form)

    def form_invalid(self, form):
        print "form not valid"
        return super(BookManualView, self).form_valid(form)
