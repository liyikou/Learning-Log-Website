from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser): 
    phone_number = models.CharField(verbose_name="Phone", max_length=11, blank=True)
    address  = models.CharField(max_length=255)