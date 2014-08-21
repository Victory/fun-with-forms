from django.views.generic import View
from django.template import RequestContext
from django.shortcuts import render_to_response

from hideyshowy.models import HideyShowyForm

class ManualView(View):
    template_name = 'hideyshowy.html'


    def get(self, request):
        hideyshowyform = HideyShowyForm()

        c = RequestContext(request, {"form": hideyshowyform})

        return render_to_response(self.template_name, c)
