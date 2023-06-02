from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def check_username(name):
    if name.lower() == 'me':
        raise ValidationError(
            'Имя пользователя не может быть <me>.'
        )


class UserNameValidator(RegexValidator):
    regex = r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$'
    message = ('Недопустимые символы в username')
    flags = 0
