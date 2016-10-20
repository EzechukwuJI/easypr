# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_general', '0004_auto_20161018_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='name',
            field=models.CharField(default=b'Press Release Distribution', max_length=175, choices=[(b'Press Release Distribution', b'Press Release Distribution'), (b'Content Writing and Marketing', b'Content Marketing'), (b'Advertising', b'Advertising'), (b'SME Marketing', b'SME Marketing'), (b'Sales and Marketing', b'Sales and Marketing'), (b'Events Bureau', b'Events Bureau'), (b'Blogger Distribution', b'Blogger Distribution')]),
        ),
    ]
