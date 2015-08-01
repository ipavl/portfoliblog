# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, help_text='Campaign display name for administrative identification.', max_length=200)),
                ('identifier', models.CharField(unique=True, help_text='The actual short part of the URL, e.g. http://www.example.com/go/<strong>[identifier]</strong>.', max_length=32)),
                ('destination', models.URLField(help_text='Where should the link go?', max_length=2048)),
            ],
        ),
    ]
