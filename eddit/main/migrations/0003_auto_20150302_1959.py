# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150302_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='phonenumber',
            new_name='phone_number',
        ),
    ]
