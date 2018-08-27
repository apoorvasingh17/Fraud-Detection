# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-27 15:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='USER',
            fields=[
                ('USER_REF', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='USER', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('NAME', models.CharField(max_length=100)),
                ('PROFILE_LINK', models.CharField(max_length=100)),
            ],
        ),
    ]
