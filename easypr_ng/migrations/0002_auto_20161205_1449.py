# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewrequest',
            name='date_closed',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='date_closed',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
