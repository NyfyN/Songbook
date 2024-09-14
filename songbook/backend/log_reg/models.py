from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    e_mail = models.EmailField(max_length=255, unique=True)

    # def save(self, *args, **kwargs):
    #     self.password = make_password(self.password)
    #     super(User, self).save(*args, **kwargs)
