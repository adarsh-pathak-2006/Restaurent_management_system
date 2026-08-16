from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES=[('MANAGER', 'MANAGER'), ('CUSTOMER', 'CUSTOMER')]
    role=models.CharField(max_length=10, choices=ROLE_CHOICES, default='CUSTOMER')


class Restaurent(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name