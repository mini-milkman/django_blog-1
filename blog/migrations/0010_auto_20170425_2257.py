# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_merge_20170425_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='headimage',
            field=models.ImageField(default='headimg/no-img.jpg', upload_to='headimg/'),
        ),
    ]
