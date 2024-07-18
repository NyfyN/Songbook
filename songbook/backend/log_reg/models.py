from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    e_mail = models.EmailField(max_length=255, unique=True)
