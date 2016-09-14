# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0002_auto_20160912_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='ordered',
            new_name='completed',
        ),
    ]
