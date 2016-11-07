# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0002_auto_20161107_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediacontact',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mediahouse',
            name='platform',
            field=models.ManyToManyField(to='easypr_ng.MediaPlatform'),
        ),
    ]
