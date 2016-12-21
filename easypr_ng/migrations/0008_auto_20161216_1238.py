# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0007_auto_20161215_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationimage',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images/publication/%Y/%M/%D', blank=True),
        ),
        migrations.AlterField(
            model_name='requestimage',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images/request/%Y/%M/%D', blank=True),
        ),
    ]
