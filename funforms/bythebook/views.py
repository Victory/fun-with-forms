from django.views.generic.edit import FormView
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from bythebook.models import BookForm, AuthorForm


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
        c = RequestContext(request, {})
        return render_to_response(self.template_name, c)

    def post(self, request):
        authors = request.POST.getlist('authors')
        titles =  request.POST.getlist('titles')

        for ii,author in enumerate(authors):
            name = author
            title = titles[ii]
            cur = {"name":name, "title": title}
            a = AuthorForm(cur)

            print a.is_valid()
            print a.errors
            print "\n\n\n\n"

        return HttpResponse("Hi")


    def form_valid(self, form):
        print "form valid"
        return super(BookManualView, self).form_valid(form)

    def form_invalid(self, form):
        print "form not valid"
        return super(BookManualView, self).form_valid(form)
