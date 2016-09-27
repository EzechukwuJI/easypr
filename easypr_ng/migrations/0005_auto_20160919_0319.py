# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0004_auto_20160919_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='prstrategy',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='prstrategy',
            name='anon_userID',
            field=models.CharField(max_length=75, verbose_name=b'Annonymous user ID'),
        ),
    ]
