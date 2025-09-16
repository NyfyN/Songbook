from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    e_mail = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.username