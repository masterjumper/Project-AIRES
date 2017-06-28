# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-27 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dj_user_client',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='dj_user_client',
            name='DJ_last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='dj_user_client',
            name='DJ_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='dj_user_client',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dj_user_client',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dj_user_client',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dj_user_client',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='dj_user_client',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dj_user_client',
            name='DJ_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='dj_user_client',
            name='DJ_id_client',
            field=models.IntegerField(unique=True),
        ),
    ]
