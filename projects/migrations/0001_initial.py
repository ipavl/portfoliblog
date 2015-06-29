# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('date', models.DateField(help_text='e.g. the date the project was started or first made publicly available.')),
                ('project_url', models.URLField(blank=True, help_text='Link to project homepage or "project overview" style pages.')),
                ('demo_url', models.URLField(blank=True, help_text='Link to somewhere the user can try the project out.')),
                ('source_url', models.URLField(blank=True, help_text='Link to public Git repo, etc.')),
                ('image', models.ImageField(blank=True, upload_to='', help_text='Logo or screenshot. Requires Pillow to be installed.')),
                ('technologies', models.CharField(max_length=128, help_text='List what the project was built with here.')),
                ('description', models.TextField(help_text='Describe what the project does. You may use Markdown here.')),
            ],
        ),
    ]
