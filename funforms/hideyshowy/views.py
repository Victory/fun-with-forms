from django.views.generic import View
from django.template import RequestContext
from django.shortcuts import render_to_response

from hideyshowy.models import HideyShowyForm

class ManualView(View):
    template_name = 'hideyshowy.html'


    def get(self, request):
        hidey_showy = HideyShowyForm()

        c = RequestContext(request)

        return render_to_response(self.template_name, c)
