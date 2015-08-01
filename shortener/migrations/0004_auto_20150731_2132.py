# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20150731_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='hits',
            field=models.BigIntegerField(editable=False, default=0),
        ),
    ]
