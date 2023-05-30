from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель пользователя."""
    email = models.EmailField(
        unique=True,
        db_index=True,
        max_length=254,
        verbose_name='Email',
        help_text='Email'
    )
    username = models.CharField(
        unique=True,
        db_index=True,
        max_length=150,
        verbose_name='Логин',
        help_text='Логин пользователя',
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
        help_text='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
        help_text='Фамилия'
    )
    password = models.CharField(
        max_length=150,
        verbose_name='Пароль',
        help_text='Пароль пользователя'
    )
    is_subcribed = models.BooleanField(
        default=False,
        verbose_name='Подписка на автора',
        help_text='Подписка на автора'
    )

    class Meta:
        ordering = ['username'],
        verbose_name = 'Пользователь',
        verbose_name = 'Пользователь'

    def __str__(self) -> str:
        return self.username
