# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-14 08:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='decription',
            new_name='description',
        ),
    ]
