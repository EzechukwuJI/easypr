# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0004_delete_mailinglist'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='blog_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
