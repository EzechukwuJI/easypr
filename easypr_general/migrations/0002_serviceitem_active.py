# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceitem',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
