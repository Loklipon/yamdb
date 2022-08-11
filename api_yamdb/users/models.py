from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    password = models.CharField(
        max_length=150,
        blank=True,
    )
    email = models.EmailField(
        max_length=150,
        unique=True,
    )
    bio = models.TextField(
        blank=True,
    )
    role = models.CharField(
        max_length=150,
        blank=True,
        choices=(
            ('user', 'user'),
            ('moderator', 'moderator'),
            ('admin', 'admin'),
        ),
        default='user',
    )
    mail_confirmation_code = models.CharField(
        max_length=150,
        blank=True,
    )
