# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_general', '0002_mailinglist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='email',
            field=models.CharField(max_length=175),
        ),
    ]
