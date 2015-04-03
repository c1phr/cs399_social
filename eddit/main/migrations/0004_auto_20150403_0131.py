# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20150302_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=4, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=4, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.IntegerField(max_length=10, serialize=False, editable=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.IntegerField(max_length=10, serialize=False, editable=False, primary_key=True),
            preserve_default=True,
        ),
    ]
