from django.db import models
from config.settings import NULLABLE
from course.models import Course


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name='Курс',
        help_text='Укажите курс',
        **NULLABLE
    )
    name = models.CharField(
        max_length=60,
        verbose_name='Название',
        help_text='Укажите название'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Напишите описание',
        **NULLABLE
    )
    photo = models.ImageField(
        upload_to='lesson/photo',
        verbose_name='Фото',
        help_text='Загрузите фото',
        **NULLABLE
    )
    url = models.URLField(
        max_length=255,
        verbose_name='Ссылка',
        help_text='Укажите ссылку',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
