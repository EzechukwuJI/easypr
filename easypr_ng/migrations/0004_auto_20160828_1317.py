# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0003_auto_20160828_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediaplatform',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
