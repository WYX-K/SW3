# Generated by Django 3.2.8 on 2022-05-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0013_delete_voteposter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headposter',
            name='username',
            field=models.CharField(default='', max_length=100, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='judgeposter',
            name='username',
            field=models.CharField(default='', max_length=100, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='poster',
            name='author_email',
            field=models.CharField(default='', max_length=100, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='preposter',
            name='username',
            field=models.CharField(default='', max_length=100, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='uicerposter',
            name='username',
            field=models.CharField(default='', max_length=100, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(default='', max_length=100, verbose_name='Username'),
        ),
    ]