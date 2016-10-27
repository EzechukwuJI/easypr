# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_general', '0008_remove_serviceitem_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceitem',
            name='action_type',
            field=models.CharField(default=b'', max_length=175, choices=[(b'select_service', b'select service'), (b'submit_content', b'submit content'), (b'request_service', b'request service')]),
        ),
    ]
