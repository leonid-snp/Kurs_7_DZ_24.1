# Generated by Django 5.0.6 on 2024-08-08 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_last_login"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 8, 8, 6, 50, 7, 450728, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Время последнего посещения",
            ),
        ),
    ]
