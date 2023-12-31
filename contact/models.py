from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=80, null=True, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.email
