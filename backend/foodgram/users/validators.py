from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def check_username(name):
    if name.lower() == 'me':
        raise ValidationError(
            'Имя пользователя не может быть <me>.'
        )


class NameValidator(RegexValidator):
    """Валидатор username."""
    regex = r'^[а-яА-ЯёЁa-zA-Z -]+$'
    message = ('Недопустимые символы в username')
    flags = 0
