from django.core.exceptions import ValidationError
from django.utils import timezone


def year_validation(value):
    """Валидатор даты выпуска."""
    if value > timezone.now().year:
        raise ValidationError(f'{value} не может быть больше текущего года.')
