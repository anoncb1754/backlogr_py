# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backlog_items', '0004_remove_backlogitem_short_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='backlogitem',
            name='list_ui_rank',
            field=models.PositiveIntegerField(default=0),
        ),
    ]