from django.shortcuts import render, get_object_or_404, HttpResponseRedirect , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Product
from .forms import UserProfileForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from django.apps import apps

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    favourite_products = profile.favourite_products.all()  # Fetch the favourite products

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'favourite_products': favourite_products,  # Add to context
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

def toggle_favourites(request, product_id):
    """ Toggle a product in user's favourites """
    UserProfile = apps.get_model('profiles', 'UserProfile')
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)
    
    if product in user_profile.favourite_products.all():
        user_profile.favourite_products.remove(product)
        is_favourite = False
        
    else:
        user_profile.favourite_products.add(product)
        is_favourite = True
        
    return JsonResponse({'is_favourite': is_favourite})


