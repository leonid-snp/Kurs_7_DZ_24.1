from django.db import models
from config.settings import NULLABLE


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

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
