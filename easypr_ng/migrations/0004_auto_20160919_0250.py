# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0003_prstrategy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prstrategy',
            old_name='annonymous_user_id',
            new_name='anon_userID',
        ),
        migrations.AlterField(
            model_name='prstrategy',
            name='target_audience_location',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
