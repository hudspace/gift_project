# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea_tracker', '0002_auto_20171005_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
