from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.template.response import TemplateResponse
from django.contrib.auth import *
from django.conf import settings

import mandrill
import logging
import forms

def index(request):
	if request.user.is_superuser:
		return render(request, 'admin/index.html')
	return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            try:
                # send the contact information via Mandrill
                m = mandrill.Mandrill(settings.MANDRILL_API_KEY)
                m.messages.send({
                    'text': form.cleaned_data.get('message'),
                    'subject': form.cleaned_data.get('subject'),
                    'from_email': form.cleaned_data.get('sender'),
                    'to': [{
                        'email': 'support@thenicepackage.com',
                        'name': 'Support',
                    }],
                })
                logging.info('Sent contact email: {0}'.format(form.cleaned_data))
            except mandrill.InvalidKeyError, e:
                logging.error('Cannot send contact email: {0}'.format(
                    form.cleaned_data))
                logging.exception(e)
            except mandrill.Error, e:
                logging.error('Cannot send contact email: {0}'.format(
                    form.cleaned_data))
                logging.exception(e)
            return redirect('contact_complete')
    else:
        form = forms.ContactForm()

    return TemplateResponse(request, 'contact.html', {
        'form' : form,
    })


def contact_complete(request):
    return TemplateResponse(request, 'contact_complete.html')


def privacy_policy(request):
    return render(request, 'privacy.html')


def careers(request):
    return render(request, 'careers.html')


def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')
