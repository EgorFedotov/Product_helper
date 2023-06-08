from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from users.validators import NameValidator, check_username


class User(AbstractUser):
    """Модель пользователя."""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    email = models.EmailField(
        unique=True,
        max_length=settings.LENGTH_FIELDS_USER,
        verbose_name='Email',
        help_text='Email'
    )
    username = models.CharField(
        unique=True,
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


class Subscription(models.Model):
    """Модель подписчика."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь',
        help_text='Пользователь',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Избранный автор',
        help_text='Избранный автор',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_relationships'
            ),
            models.CheckConstraint(
                name='prevent_self_follow',
                check=~models.Q(user=models.F('author')),
            ),
        ]

    def __str__(self):
        return f'{self.user} {self.author}'
