# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(null=True, upload_to=b'media/publicaton_image/%Y-%M-%D', blank=True)),
                ('caption', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='pubdocument',
            name='publication',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='pictures',
        ),
        migrations.DeleteModel(
            name='PubDocument',
        ),
        migrations.AddField(
            model_name='publication',
            name='pictures',
            field=models.ManyToManyField(to='easypr_ng.PublicationImage'),
        ),
    ]
