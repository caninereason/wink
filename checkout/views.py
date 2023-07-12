from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51NSiZhGucOKJFPCDAXSI5L8DomX4bNr6Reb4JpR8ymLywW6NJ688pQnNDd91nVVXinCaTaxl0Fn0b02y63WrX1v500buKotRNb',
        'client_secret':'test client secret',
    }

    return render(request, template, context)