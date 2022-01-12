from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class NumberModel():
    userNumber = models.AutoField(primary_key=True)

class User(AbstractUser, NumberModel):

    # name = models.CharField(blank=True, max_length=255)
    # userId = models.CharField(blank=False, max_length=255)
    password = models.CharField(blank=False, max_length=255)


    def get_absolute_url(self):

        return reverse("users:detail", kwargs={"username": self.username})
