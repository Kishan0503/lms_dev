from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (('STUDENT', 'Student'), ('LIBRARIAN', 'Librarian'))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, blank=True, null=True)

class Author(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

class Genre(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)