# Generated by Django 5.2.1 on 2025-05-11 14:02

import django.db.models.deletion
import taska_app.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taska_app', '0005_rename_taskitem_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='due_date',
            field=models.DateTimeField(default=taska_app.models.one_week_hence),
        ),
        migrations.AddField(
            model_name='projects',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
