# Generated by Django 3.2.8 on 2022-05-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0007_alter_poster_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='file',
            field=models.ImageField(default='', upload_to='', verbose_name='File'),
        ),
    ]