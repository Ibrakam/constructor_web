# Generated by Django 5.0.6 on 2024-07-06 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modul', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot',
            name='subscription_chats_changed_at',
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.BigIntegerField(default=1528636691, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usertg',
            name='last_interaction',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 6, 15, 48, 15, 86334, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]