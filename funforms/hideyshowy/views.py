from django.shortcuts import render

from django.views.generic import TemplateView, View


class ManualView(TemplateView):
    template_name = 'hideyshowy.html'
