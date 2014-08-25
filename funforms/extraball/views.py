from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView
from django.views.generic import TemplateView, View



class ExtraBallView(SessionWizardView):
    def done(self, form_list, **kwargs):
        # TODO: Make this a redirect
        return render_to_response('done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

class DoneView(TemplateView):
    template_name = 'extraball-done.html'
