# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 09:51
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171123_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passage',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]