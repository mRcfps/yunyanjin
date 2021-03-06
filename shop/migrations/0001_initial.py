# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-24 09:31
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
                ('unit', models.CharField(max_length=10, verbose_name='单位')),
                ('stock', models.PositiveIntegerField(verbose_name='库存')),
            ],
            options={
                'verbose_name_plural': '购买项目',
                'verbose_name': '购买项目',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/', verbose_name='照片')),
            ],
            options={
                'verbose_name_plural': '商品照片',
                'verbose_name': '商品照片',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='名称')),
                ('image', models.ImageField(blank=True, upload_to='products/', verbose_name='照片')),
                ('description', models.TextField(blank=True, verbose_name='简介')),
                ('info', models.TextField(blank=True, verbose_name='详细信息')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='上架时间')),
            ],
            options={
                'verbose_name_plural': '商品',
                'verbose_name': '商品',
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='shop.Product', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.Product', verbose_name='商品'),
        ),
    ]
