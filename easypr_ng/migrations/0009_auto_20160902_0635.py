# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0008_auto_20160902_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paydetails',
            name='user',
            field=models.ForeignKey(verbose_name=b'Payment By', to=settings.AUTH_USER_MODEL),
        ),
    ]
