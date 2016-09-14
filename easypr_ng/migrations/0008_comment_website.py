# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0007_auto_20160913_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='website',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
