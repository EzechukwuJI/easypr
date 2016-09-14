# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='publication',
            field=models.OneToOneField(to='easypr_ng.Publication'),
        ),
    ]
