# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-07 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NguoiDung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
                ('lastcontact', models.DateTimeField(auto_now_add=True)),
                ('topic', models.CharField(max_length=100)),
                ('status', models.IntegerField(max_length=100)),
            ],
        ),
    ]
