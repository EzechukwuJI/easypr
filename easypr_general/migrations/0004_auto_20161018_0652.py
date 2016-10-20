# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_general', '0003_auto_20161018_0650'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='ServiceCategory',
        ),
    ]
