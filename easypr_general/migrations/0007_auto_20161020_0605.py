# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_general', '0006_serviceitem_call_to_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceitem',
            name='icon_text',
            field=models.CharField(max_length=75, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='serviceitem',
            name='call_to_action',
            field=models.CharField(max_length=75, null=True, blank=True),
        ),
    ]
