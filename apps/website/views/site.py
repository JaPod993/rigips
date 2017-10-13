# -*- encoding: utf-8 -*-
from django.shortcuts import redirect
from django.views.generic import FormView
from website.forms.registration_form import RegistrationForm
from website.models.configuration import Configuration
from website.models.registration import RegistrationFile
from django.contrib import messages
import magic


class HomepePageView(FormView):
    template_name = 'website/site/homepage.html'
    form_class = RegistrationForm
    ALLOW_MIME_TYPES = ['image/png', 'image/jpeg']
    ALLOW_MIME_TYPES_SCAN = ALLOW_MIME_TYPES + ['application/pdf', 'application/x-pdf']

    def get_context_data(self, **kwargs):
        context = super(HomepePageView, self).get_context_data(**kwargs)
        context["configuration"] = Configuration.get_solo()
        return context

    def form_invalid(self, form):
        messages.error(self.request, u'Formularz zawiera błędy', extra_tags='error')
        return super(HomepePageView, self).form_invalid(form)

    def get_success_url(self):
        return "/"

    def form_valid(self, form):

        obj = form.save(commit=False)

        all_files_ok = True
        files_list = self.request.FILES.getlist('files')

        if len(files_list) > 5:
            form.add_error('files', u'Dopuszczalna ilość plików to 5')
            messages.error(self.request, u'Formularz zawiera błędy', extra_tags='error')
            return self.form_invalid(form)

        scan_file = self.request.FILES.get('allow_scan')
        if scan_file:
            if magic.from_buffer(scan_file.read(1024), mime=True) not in self.ALLOW_MIME_TYPES_SCAN or scan_file.size > 5000000:
                all_files_ok = False
                form.add_error('allow_scan', u'Niewłaściwy format pliku lub zbyt duży plik')

        for f in files_list:
            if magic.from_buffer(f.read(1024), mime=True) not in self.ALLOW_MIME_TYPES:
                all_files_ok = False

            if f.size > 5000000:
                all_files_ok = False

        if all_files_ok:
            obj.save()

            for f in self.request.FILES.getlist('files'):
                RegistrationFile(registration=obj, file=f).save()

            messages.success(self.request, u'Pomyślnie wysłano zgłoszenie', extra_tags='success')
        else:
            form.add_error('files', u'Błędny format lub zbyt duzy plik')
            messages.error(self.request, u'Formularz zawiera błędy', extra_tags='error')
            return self.form_invalid(form)

        return super(HomepePageView, self).form_valid(form)