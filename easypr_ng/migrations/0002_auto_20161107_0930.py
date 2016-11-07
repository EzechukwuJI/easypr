# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bouquet',
            name='media_houses',
        ),
        migrations.RemoveField(
            model_name='bouquet',
            name='press_material',
        ),
        migrations.DeleteModel(
            name='Bouquet',
        ),
    ]
