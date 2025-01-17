# Generated by Django 5.0.6 on 2024-07-11 09:54

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modul', '0004_alter_user_uid_alter_usertg_last_interaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leomatchmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.BigIntegerField(default=3319636879, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usertg',
            name='last_interaction',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 11, 9, 54, 37, 691030, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
