# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-25 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_listing', '0008_remove_book_list_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book_list',
            old_name='uploaded_by',
            new_name='author',
        ),
    ]