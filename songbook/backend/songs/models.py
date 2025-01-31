from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Tab(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)  # RRGGBB
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('PDF', 'PDF'),
        ('WAV', 'WAV'),
    ]
    title = models.CharField(max_length=255),
    pdf_file = models.FileField(
        upload_to='song/pdfs/',
        null=True,
        blank=True)
    sample_file = models.FileField(
        upload_to='song/wavs/',
        null=True,
        blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    document_type = models.CharField(
        max_length=3, choices=DOCUMENT_TYPE_CHOICES)
