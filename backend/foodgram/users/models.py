from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from users.validators import NameValidator, check_username


class User(AbstractUser):
    """Модель пользователя."""
    email = models.EmailField(
        unique=True,
        max_length=settings.LENGTH_FIELDS_USER,
        verbose_name='Email',
        help_text='Email'
    )
    username = models.CharField(
        unique=True,
        db_index=True,
        max_length=settings.LENGTH_FIELDS_USER,
        verbose_name='Логин',
        help_text='Логин пользователя',
        validators=[check_username,
                    UnicodeUsernameValidator()
                    ]
    )
    first_name = models.CharField(
        max_length=settings.LENGTH_FIELDS_USER,
        verbose_name='Имя',
        help_text='Имя',
        validators=[NameValidator()]
    )
    last_name = models.CharField(
        max_length=settings.LENGTH_FIELDS_USER,
        verbose_name='Фамилия',
        help_text='Фамилия',
        validators=[NameValidator()]
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
