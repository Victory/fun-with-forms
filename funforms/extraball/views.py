from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView
from django.views.generic import TemplateView, View

from extraball.models import ExtraBallForm1, ExtraBallForm2, ExtraBallForm3

class ExtraBallView(SessionWizardView):
    form_list =  [ExtraBallForm1, ExtraBallForm2, ExtraBallForm3]
    template_name = 'extraball.html'
    def done(self, form_list, **kwargs):
        # TODO: Make this a redirect
        return render_to_response('extraball-done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

class DoneView(TemplateView):
    template_name = 'extraball-done.html'
