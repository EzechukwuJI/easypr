# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0005_auto_20160919_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prstrategy',
            name='business_type',
            field=models.CharField(default=b'Company', max_length=25, choices=[(b'NA', b'NA'), (b'Company', b'Company'), (b'Individual', b'Individual')]),
        ),
        migrations.AlterField(
            model_name='prstrategy',
            name='company_type',
            field=models.CharField(default=b'Private', max_length=75, choices=[(b'NA', b'NA'), (b'Public', b'Public'), (b'Private', b'Private')]),
        ),
        migrations.AlterField(
            model_name='prstrategy',
            name='frequency_of_pr',
            field=models.CharField(default=b'monthly', max_length=100, choices=[(b'NA', b'NA'), (b'weekly', b'Weekly'), (b'monthly', b'Monthly'), (b'several-times-a-month', b'Several Times a Month'), (b'quartely', b'Quartely'), (b'annually', b'Annually'), (b'first-time-user', b'First Time User')]),
        ),
    ]
