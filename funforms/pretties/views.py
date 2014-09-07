from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView


class PrettiesView(TemplateView):
    template_name = "pretties.html"
