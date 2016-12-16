# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0005_blogs_blog_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'verbose_name_plural': 'Blogs'},
        ),
        migrations.AddField(
            model_name='blogs',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
