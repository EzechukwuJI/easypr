# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_general', '0003_auto_20161208_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='name',
            field=models.CharField(default=b'Press Release Distribution', max_length=175, choices=[(b'Press Release Distribution', b'Press Release Distribution'), (b'Content Writing and Marketing', b'Content Marketing'), (b'Advertising', b'Advertising'), (b'SME Start Up Toolkit', b'SME Start Up Toolkit'), (b'Sales and Marketing', b'Sales and Marketing'), (b'Events Bureau', b'Events Bureau'), (b'Blogger Distribution', b'Blogger Distribution')]),
        ),
    ]
