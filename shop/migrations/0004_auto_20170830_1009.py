# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 10:09
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170824_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='info',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='详细信息'),
        ),
    ]