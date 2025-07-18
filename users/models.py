from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(blank=True, null=True, verbose_name="Biografia")
    connections = models.ManyToManyField("self", blank=True, symmetrical=True)
    birth_date = models.DateField(blank=True, null=True)
