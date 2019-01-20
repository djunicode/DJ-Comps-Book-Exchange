# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-07 10:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("forum", "0007_merge_20180107_1531")]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="date_created",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(
                    2018, 1, 7, 10, 2, 27, 812009, tzinfo=utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="date_created",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(
                    2018, 1, 7, 10, 2, 27, 812009, tzinfo=utc
                )
            ),
        ),
    ]
