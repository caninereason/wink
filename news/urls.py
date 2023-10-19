from django.urls import path
from . import views

urlpatterns = [
    path('toggle-newsletter/', views.toggle_newsletter_subscription, name='toggle-newsletter'),
    # ... other url patterns ...
]
