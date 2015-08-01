# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_shorturl_hits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='hits',
            field=models.IntegerField(editable=False),
        ),
    ]
