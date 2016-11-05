# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0002_auto_20161102_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='paydetails',
            name='currency',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
