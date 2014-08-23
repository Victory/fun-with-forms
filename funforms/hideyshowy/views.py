from django.views.generic import View
from django.template import RequestContext
from django.shortcuts import render_to_response

from hideyshowy.models import HideyShowyForm


class ManualView(View):
    template_name = 'hideyshowy.html'
    form = HideyShowyForm

    def get(self, request):
        c = RequestContext(request, {"form": self.form()})

        return render_to_response(self.template_name, c)


    def post(self, request):

        form = self.form(request.POST)

        if form.is_valid():
            form.save()

        c = RequestContext(request, {"form": form})

        return render_to_response(self.template_name, c)
