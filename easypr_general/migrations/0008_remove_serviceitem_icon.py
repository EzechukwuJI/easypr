# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_general', '0007_auto_20161020_0605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceitem',
            name='icon',
        ),
    ]
