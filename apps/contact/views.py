from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from forms import ContactForm


def contact(request):
    """Send email to settings.MANAGERS"""
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                'A form from %s' % (cd['name']),
                cd['message'],
                cd['email'],
                [mail_tuple[1] for mail_tuple in settings.MANAGERS],
            )
            success = True
    else:
        form = ContactForm()

    return render_to_response(
        'contact/contact.html',
        {'form': form, 'success': success},
        context_instance=RequestContext(request)
    )
