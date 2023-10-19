from django.db import models
from django.contrib.auth.models import User

class NewsletterSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=False)

    @property
    def email(self):
        return self.user.email
