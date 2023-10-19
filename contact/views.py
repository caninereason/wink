from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

from django.core.mail import send_mail

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Extract data from the form
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email to you (or your support team)
            send_mail(
                subject=f"Contact message from {email}: {subject}",
                message=message,
                from_email=email,
                recipient_list=['naraxa4790@wisnick.com'],  # Replace with your email
            )

            # Send a thank you email to the user
            send_mail(
                subject="Thank You for Your Query",
                message="Thank you for your query. We will endeavor to contact you regarding your questions as soon as possible.",
                from_email="wink.com",
                recipient_list=[email],
            )

            return render(request, 'contact/success.html')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact/contact.html', context)

