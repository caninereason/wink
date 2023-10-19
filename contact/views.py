from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Extract data from the form
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f"Contact message from {name}",
                message=message,
                from_email=email,
                recipient_list=['naraxa4790@wisnick.com'],  # Replace with your email
            )
            send_mail(
                            subject=f"Thank You for your query",
                            message=f"Thank You for your query, we will endeavor to contact you regarding your questions as soon as possible",
                            from_email=f"wink.com",
                            recipient_list=['email'],  # Replace with your email
                        )
            return render(request, 'contact/success.html')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact/contact.html', context)
