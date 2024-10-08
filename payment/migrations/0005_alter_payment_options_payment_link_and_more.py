# Generated by Django 5.0.6 on 2024-07-23 06:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0004_remove_payment_paid_course_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="payment",
            options={"verbose_name": "Платеж", "verbose_name_plural": "Платежи"},
        ),
        migrations.AddField(
            model_name="payment",
            name="link",
            field=models.URLField(
                blank=True,
                help_text="Укажите ссылку на оплату",
                max_length=400,
                null=True,
                verbose_name="Ссылка на оплату",
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="session_id",
            field=models.CharField(
                blank=True,
                help_text="Укажите id сессии",
                max_length=255,
                null=True,
                verbose_name="Id сессии",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="users",
            field=models.ForeignKey(
                help_text="Укажите пользователя",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]
