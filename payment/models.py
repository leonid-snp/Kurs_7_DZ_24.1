from django.db import models
from config.settings import NULLABLE
from course.models import Course
from lesson.models import Lesson
from users.models import User


class Payment(models.Model):
    users = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Укажите пользователя',
    )
    date_payment = models.DateField(
        auto_now_add=True,
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name='Курс',
        help_text='укажите курс',
        **NULLABLE
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name='Урок',
        help_text='Укажите урок',
        **NULLABLE
    )
    sum = models.PositiveIntegerField(
        verbose_name='Сумма',
        help_text='Укажите сумму',
        **NULLABLE
    )
    cash_payment = models.BooleanField(
        verbose_name='Наличные',
        help_text='Выберите наличные',
        **NULLABLE
    )
    payment_to_account = models.BooleanField(
        verbose_name='Перевод',
        help_text='Выберите перевод на счет',
        **NULLABLE
    )
