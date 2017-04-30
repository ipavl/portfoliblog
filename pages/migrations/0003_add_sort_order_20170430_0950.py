# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_show_in_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='menu_sort_order',
            field=models.IntegerField(default=0, help_text='Sort order of the link if displaying in the main site navigation. Lowest-to-highest = left-to-right.'),
        ),
        migrations.AlterField(
            model_name='page',
            name='show_in_menu',
            field=models.BooleanField(help_text='If checked, will display this page as a link in the main site navigation.'),
        ),
    ]
