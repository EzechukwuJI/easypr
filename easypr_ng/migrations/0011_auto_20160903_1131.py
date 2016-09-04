# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0010_auto_20160903_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='post_id',
            new_name='transaction_id',
        ),
    ]
