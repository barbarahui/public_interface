# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-06 06:02
from __future__ import unicode_literals

from django.db import migrations
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exhibits', '0018_auto_20160406_0544'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibititem',
            name='lesson_plan_order',
            field=positions.fields.PositionField(default=-1),
        ),
    ]
