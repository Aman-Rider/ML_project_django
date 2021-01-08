from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
# Create your models here.

class CustomUser(AbstractUser):
    mobile = PhoneField(blank=True, help_text='Contact phone number')
    country = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username