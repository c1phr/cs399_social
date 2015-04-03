# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150403_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upvotes',
            field=models.IntegerField(default=0, max_length=6),
            preserve_default=True,
        ),
    ]
