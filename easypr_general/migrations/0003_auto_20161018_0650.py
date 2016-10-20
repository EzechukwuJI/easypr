# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_general', '0002_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('name_slug', models.CharField(max_length=175)),
                ('icon', models.FileField(null=True, upload_to=b'services_icon', blank=True)),
                ('image', models.FileField(null=True, upload_to=b'services_image', blank=True)),
                ('description', models.TextField(max_length=750)),
            ],
        ),
        migrations.RemoveField(
            model_name='services',
            name='category',
        ),
        migrations.RemoveField(
            model_name='services',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='services',
            name='image',
        ),
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(default=b'Press Release Distribution', max_length=175, choices=[(b'press-distribution', b'Press Release Distribution'), (b'content-marketing', b'Content Marketing'), (b'advertising', b'Advertising'), (b'sme-marketing', b'SME Marketing'), (b'sales_n_marketing', b'Sales and Marketing'), (b'events-bureau', b'Events Bureau'), (b'blogger-distribution', b'Blogger Distribution')]),
        ),
        migrations.AddField(
            model_name='serviceitem',
            name='category',
            field=models.ForeignKey(to='easypr_general.Services'),
        ),
    ]
