# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-20 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20180220_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='portada',
            field=models.ImageField(blank=True, default='portada01.png', null=True, upload_to='portadas'),
        ),
    ]
