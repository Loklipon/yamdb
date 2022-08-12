from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Никнейм пользователя (обязательно):'
    )
    password = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Пароль'
    )
    email = models.EmailField(
        max_length=150,
        unique=True,
        verbose_name='Адрес электронной почты (обязательно):'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Информация о пользователе'
    )
    role = models.CharField(
        max_length=150,
        blank=True,
        choices=(
            ('user', 'Пользователь'),
            ('moderator', 'Модератор'),
            ('admin', 'Администратор'),
        ),
        default='user',
        verbose_name='Право управления'
    )
    mail_confirmation_code = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Код подтверждеиня адреса электронной почты'
    )

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=('username', 'email'), name='unique_following')]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
       
