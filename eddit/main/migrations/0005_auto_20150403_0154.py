# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150403_0131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_content',
            new_name='post_link',
        ),
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.TextField(default='Test', max_length=50),
            preserve_default=False,
        ),
    ]
