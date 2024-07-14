from django.db import models
from config.settings import NULLABLE
from users.models import User


class Course(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name='Название',
        help_text='Укажите название'
    )
    photo = models.ImageField(
        upload_to='course/photo',
        verbose_name='Фото',
        help_text='Загрузите фото',
        **NULLABLE
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Напишите описание',
        **NULLABLE
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Автор',
        help_text='Укажите автора курса',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
