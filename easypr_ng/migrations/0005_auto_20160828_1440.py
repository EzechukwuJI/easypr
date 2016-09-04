# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0004_auto_20160828_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bouquet',
            old_name='Num_of_media',
            new_name='num_of_media',
        ),
    ]
