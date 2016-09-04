# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0009_auto_20160902_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='post_id',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publicationimage',
            name='caption',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
