# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-04 18:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_song_song_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
