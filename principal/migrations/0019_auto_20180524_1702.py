# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0018_auto_20180524_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='IdClase',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
