from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    email_otp = models.CharField(max_length=6, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
