from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from bythebook.models import BookForm


class BookView(FormView):
    template_name = 'book.html'
    form_class = BookForm
    success_url = '/book-added'

    def form_valid(self, form):
        form.save(self.request, True)
        return super(BookView, self).form_valid(form)


class BookAddedView(TemplateView):
    template_name = 'book-added.html'


class BookManualView(FormView):
    form_class = BookForm
    template_name = 'manual.html'
    success_url = '/manual'

    def get_context_data(self, **kwargs):
        context = super(BookManualView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        print "form valid"
        return super(BookManualView, self).form_valid(form)

    def form_invalid(self, form):
        print "form not valid"
        return super(BookManualView, self).form_valid(form)
