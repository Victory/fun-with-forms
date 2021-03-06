from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView
from django.views.generic import TemplateView

from extraball.models import ExtraBallForm1, ExtraBallForm2, ExtraBallForm3


class ExtraBallView(SessionWizardView):
    form_list = [ExtraBallForm1, ExtraBallForm2, ExtraBallForm3]
    template_name = 'extraball.html'

    def get_form_initial(self, step):
        current_step = int(self.storage.current_step)
        initial = {}

        if current_step == 0:
            print "HERE"
            prev_data = self.storage.get_step_data('0')
            if prev_data:
                subject = prev_data.get('0-subject', '')
                initial = {"message": "%s\n----------\n" % subject}

        return self.initial_dict.get(step, initial)

    def get_context_data(self, form, **kwargs):
        context = super(ExtraBallView, self).get_context_data(form, **kwargs)

        extra_data = {}
        current_step = int(self.storage.current_step)

        if current_step == 2:
            prev_data = self.storage.get_step_data('1')
            extra_data['message_val'] = prev_data.get('1-message', '')
            context.update(extra_data)

        return context

    def done(self, form_list, **kwargs):
        # TODO: Make this a redirect
        return render_to_response('extraball-done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


class DoneView(TemplateView):
    template_name = 'extraball-done.html'
