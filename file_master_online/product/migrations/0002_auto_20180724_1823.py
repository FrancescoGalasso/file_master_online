# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-07-24 16:23
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='text',
        ),
        migrations.AddField(
            model_name='product',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=''),
        ),
    ]