from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView
from django.views.generic import TemplateView, View

from extraball.models import ExtraBallForm1, ExtraBallForm2, ExtraBallForm3

class ExtraBallView(SessionWizardView):
    form_list =  [ExtraBallForm1, ExtraBallForm2, ExtraBallForm3]
    template_name = 'extraball.html'



    def get_context_data(self, form, **kwargs):
        context = super(ExtraBallView, self).get_context_data(form, **kwargs)

        extra_data = {}
        current_step = int(self.storage.current_step)
        if current_step == 1:
            prev_data = self.storage.get_step_data('0')
            extra_data['subject_val'] = prev_data.get('0-subject','')
            context.update(extra_data)

        if current_step == 2:
            prev_data = self.storage.get_step_data('1')
            extra_data['message_val'] = prev_data.get('1-message','')
            context.update(extra_data)

        return context

    def done(self, form_list, **kwargs):
        # TODO: Make this a redirect
        return render_to_response('extraball-done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

class DoneView(TemplateView):
    template_name = 'extraball-done.html'
