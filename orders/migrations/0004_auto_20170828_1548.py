# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-28 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20170828_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False, verbose_name='订单编号'),
        ),
    ]
