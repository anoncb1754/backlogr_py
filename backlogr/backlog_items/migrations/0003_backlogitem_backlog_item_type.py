# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backlog_items', '0002_auto_20160331_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='backlogitem',
            name='backlog_item_type',
            field=models.CharField(choices=[('user_story', 'user_story'), ('epic', 'epic'), ('non_functional_requirement', 'non_functional_requirement')], db_index=True, default='user_story', max_length=50),
        ),
    ]