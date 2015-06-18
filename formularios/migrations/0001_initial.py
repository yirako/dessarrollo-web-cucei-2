# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=32)),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('passw', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('pagweb', models.URLField()),
            ],
        ),
    ]
