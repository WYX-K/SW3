# Generated by Django 3.2.8 on 2022-05-07 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0015_remove_uicerposter_votestatus'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PrePoster',
        ),
    ]