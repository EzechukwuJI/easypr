# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'Press Release Distribution', max_length=175, choices=[(b'press-distribution', b'Press Release Distribution'), (b'content-marketing', b'Content Marketing'), (b'advertising', b'Advertising'), (b'sme-marketing', b'SME Marketing'), (b'sales_n_marketing', b'Sales and Marketing'), (b'events-bureau', b'Events Bureau'), (b'blogger-distribution', b'Blogger Distribution')])),
                ('name', models.CharField(max_length=100)),
                ('name_slug', models.CharField(max_length=175)),
                ('icon', models.FileField(null=True, upload_to=b'services_icon', blank=True)),
                ('image', models.FileField(null=True, upload_to=b'services_image', blank=True)),
                ('description', models.TextField(max_length=750)),
            ],
        ),
    ]
