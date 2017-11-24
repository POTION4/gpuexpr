# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('author', models.CharField(max_length=1024)),
                ('body', models.TextField()),
            ],
        ),
    ]