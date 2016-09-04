# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0011_auto_20160903_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='bouquet',
            name='discounted_price_per_media_D',
            field=models.FloatField(default=0.0, verbose_name=b'Discounted Price Dollar'),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='discounted_price_per_media_N',
            field=models.FloatField(default=0.0, verbose_name=b'Discounted Price Naira'),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='percentage_savings',
            field=models.FloatField(default=0.0),
        ),
    ]
