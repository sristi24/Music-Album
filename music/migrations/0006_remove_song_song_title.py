# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-04 18:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='song_title',
        ),
    ]
