# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='first_visit',
            field=models.DateField(default=datetime.datetime(2016, 1, 7, 15, 39, 46, 355760)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='last_visit',
            field=models.DateField(default=datetime.datetime(2016, 1, 7, 15, 39, 46, 355800)),
            preserve_default=True,
        ),
    ]
