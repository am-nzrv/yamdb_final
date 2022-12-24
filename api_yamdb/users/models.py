from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    ROLE_CHOICES = [
        (USER, 'User'),
        (ADMIN, 'Administrator'),
        (MODERATOR, 'Moderator'),
    ]

    bio = models.TextField(
        verbose_name='Биография',
        null=True,
        blank=True
    )
    role = models.TextField(
        verbose_name='Роль',
        choices=ROLE_CHOICES,
        default=USER,
        blank=True
    )

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.CheckConstraint(
                check=~models.Q(username__iexact='me'),
                name='username_is_not_me'
            ),
        ]

    def __str__(self):
        return self.username[:15]
