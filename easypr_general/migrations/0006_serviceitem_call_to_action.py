# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_general', '0005_auto_20161019_0640'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceitem',
            name='call_to_action',
            field=models.CharField(default='', max_length=75),
            preserve_default=False,
        ),
    ]
