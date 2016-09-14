# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0003_auto_20160912_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='paydetails',
            name='date_verified',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paydetails',
            name='pay_status',
            field=models.CharField(default=b'pending', max_length=25, choices=[(b'verified', b'verified'), (b'pending', b'pending'), (b'failed', b'failed')]),
        ),
        migrations.AddField(
            model_name='paydetails',
            name='verified_by',
            field=models.BooleanField(default=False),
        ),
    ]
