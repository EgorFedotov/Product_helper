from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from foodgram.settings import LENGTH_FIELDS_USER

from users.validators import UserNameValidator, check_username


class User(AbstractUser):
    """Модель пользователя."""
    email = models.EmailField(
        unique=True,
        db_index=True,
        max_length=LENGTH_FIELDS_USER,
        verbose_name='Email',
        help_text='Email'
    )
    username = models.CharField(
        unique=True,
        db_index=True,
        max_length=LENGTH_FIELDS_USER,
        verbose_name='Логин',
        help_text='Логин пользователя',
        validators=[check_username,
                    UnicodeUsernameValidator()
                    ]
    )
    first_name = models.CharField(
        max_length=LENGTH_FIELDS_USER,
        verbose_name='Имя',
        help_text='Имя',
        validators=[UserNameValidator]
    )
    last_name = models.CharField(
        max_length=LENGTH_FIELDS_USER,
        verbose_name='Фамилия',
        help_text='Фамилия',
        validators=[UserNameValidator]
    )
    password = models.CharField(
        max_length=LENGTH_FIELDS_USER,
        verbose_name='Пароль',
        help_text='Пароль пользователя'
    )
    is_subcribed = models.BooleanField(
        default=False,
        verbose_name='Подписка на автора',
        help_text='Подписка на автора'
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
