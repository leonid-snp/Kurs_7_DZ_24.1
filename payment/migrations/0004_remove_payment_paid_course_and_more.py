# Generated by Django 5.0.6 on 2024-07-23 05:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0002_course_author"),
        ("lesson", "0003_lesson_author"),
        ("payment", "0003_alter_payment_paid_course_alter_payment_paid_lesson"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="paid_course",
        ),
        migrations.RemoveField(
            model_name="payment",
            name="paid_lesson",
        ),
        migrations.RemoveField(
            model_name="payment",
            name="users",
        ),
        migrations.AddField(
            model_name="payment",
            name="paid_course",
            field=models.ForeignKey(
                blank=True,
                help_text="укажите курс",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="course.course",
                verbose_name="Курс",
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="paid_lesson",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите урок",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="lesson.lesson",
                verbose_name="Урок",
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="users",
            field=models.ForeignKey(
                default=None,
                help_text="Укажите пользователя",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]
