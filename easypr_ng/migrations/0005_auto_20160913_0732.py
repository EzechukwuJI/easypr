# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0004_auto_20160912_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='media_urls',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='pictures',
        ),
        migrations.AddField(
            model_name='publicationimage',
            name='post',
            field=models.ForeignKey(blank=True, to='easypr_ng.Publication', null=True),
        ),
        migrations.AddField(
            model_name='redirect_url',
            name='post',
            field=models.ForeignKey(blank=True, to='easypr_ng.Publication', null=True),
        ),
    ]
