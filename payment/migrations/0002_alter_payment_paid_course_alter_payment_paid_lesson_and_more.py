# Generated by Django 5.0.6 on 2024-07-11 07:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0001_initial"),
        ("lesson", "0002_alter_lesson_options"),
        ("payment", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="paid_course",
            field=models.ManyToManyField(
                help_text="укажите курс", to="course.course", verbose_name="Курс"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="paid_lesson",
            field=models.ManyToManyField(
                help_text="Укажите урок", to="lesson.lesson", verbose_name="Урок"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="users",
            field=models.ManyToManyField(
                help_text="Укажите пользователя",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]
