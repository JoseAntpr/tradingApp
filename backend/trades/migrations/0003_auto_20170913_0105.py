# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0002_auto_20170911_1206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trade',
            options={'ordering': ['-date_booked']},
        ),
        migrations.AlterField(
            model_name='trade',
            name='rate',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]