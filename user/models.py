from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse_lazy

from general.models import location_choices


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=50, choices=location_choices)
    about = models.TextField(null=True)

    class Meta:
        ordering = ['last_name']

    def get_absolute_url(self):
        return reverse_lazy('profile')

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
