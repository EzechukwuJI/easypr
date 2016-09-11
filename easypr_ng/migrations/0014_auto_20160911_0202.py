# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0013_auto_20160904_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paydetails',
            name='date_paid',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
