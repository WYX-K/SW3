# Generated by Django 3.2.8 on 2022-05-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0002_remove_poster_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='grade',
            field=models.IntegerField(default=0, verbose_name='Grade'),
        ),
    ]
