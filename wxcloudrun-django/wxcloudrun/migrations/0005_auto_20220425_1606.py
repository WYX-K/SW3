# Generated by Django 3.2.8 on 2022-04-25 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxcloudrun', '0004_auto_20220412_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counters',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 25, 16, 6, 44, 976750)),
        ),
        migrations.AlterField(
            model_name='counters',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 25, 16, 6, 44, 976770)),
        ),
    ]