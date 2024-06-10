import uuid
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']


class Place(models.Model):
    name = models.CharField(max_length=255, null=False)
    photo = models.FileField(upload_to='photos')
    descriptions = models.TextField(null=True)
    coordinate = models.CharField(max_length=255, null=False)


class Trip(models.Model):
    name = models.CharField(max_length=255, null=False)
    places = models.ManyToManyField(Place)




