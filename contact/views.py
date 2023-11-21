from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


def contact(request):
    contactForm = ContactForm()

    if request.method == "POST":
        contactForm = ContactForm(request.POST or None)

        if contactForm.is_valid():
            contactForm.save()

            subject = contactForm.cleaned_data.get('subject')
            message = contactForm.cleaned_data.get('message')

            # sending mail

            send_mail(
                subject,  # subject
                message,  # message
                'settings.EMAIL_HOST_USER',  # from mail
                ['youremail@gmail.com', ],  # to mail
                fail_silently=False,
            )

            return redirect("contact:contact")

    context = {
        "contact": contactForm
    }

    return render(request, 'blog/contact.html', context)
