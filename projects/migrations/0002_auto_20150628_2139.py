# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(help_text='Describe what the project does. You may use Markdown.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(unique=True, max_length=200, help_text='Text to be shown in the URL for this item. Auto-populates based on the name field.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=models.CharField(help_text='List what the project was built with here.', max_length=200),
        ),
    ]
