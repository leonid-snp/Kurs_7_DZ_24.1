from django.utils.timezone import now

from django.contrib.auth.models import AbstractUser
from django.db import models
from config.settings import NULLABLE


class User(AbstractUser):
    username = None

    last_login = models.DateTimeField(
        default=now,
        verbose_name="Время последнего посещения",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Почта",
        help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        help_text="Укажите телефон",
        **NULLABLE
    )
    city = models.CharField(
        max_length=60,
        verbose_name="Город",
        help_text="Укажите город",
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загрузите аватар",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
