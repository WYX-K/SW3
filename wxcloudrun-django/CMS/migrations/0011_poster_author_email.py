# Generated by Django 3.2.8 on 2022-05-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0010_poster_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='author_email',
            field=models.CharField(default='', max_length=20, verbose_name='Username'),
        ),
    ]