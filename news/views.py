from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import NewsletterSubscription

def toggle_newsletter_subscription(request):

    context = {}
    if hasattr(request.user, 'newslettersubscription'):
        context['subscribed'] = request.user.newslettersubscription.subscribed
    else:
        context['subscribed'] = False
    
    if request.user.is_authenticated:
        subscription, created = NewsletterSubscription.objects.get_or_create(user=request.user)
        
        # Toggle the subscription status
        subscription.subscribed = not subscription.subscribed
        subscription.save()

        # Send email if subscribing
        if subscription.subscribed:
            send_mail(
                "Thank you for subscribing!",
                "You've successfully subscribed to our newsletter.",
                "from_email@example.com",  # Replace with your email
                [request.user.email],
                fail_silently=False,
            )
            messages.success(request, 'Successfully subscribed to the newsletter!')
        else:
            messages.success(request, 'Successfully unsubscribed from the newsletter!')

    else:
        messages.error(request, 'You need to be logged in to subscribe.')

    return redirect(request.META.get('HTTP_REFERER', 'default_redirect_url'))
