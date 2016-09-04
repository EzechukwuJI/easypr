# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0002_auto_20160828_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaPlatform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_slug', models.CharField(max_length=75)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_slug', models.CharField(max_length=75)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='mediahouse',
            name='platform',
        ),
        migrations.AddField(
            model_name='mediahouse',
            name='platform',
            field=models.ManyToManyField(to='easypr_ng.MediaPlatform', blank=True),
        ),
    ]
