# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('easypr_ng', '0006_auto_20160913_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('reply', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='posted_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentreply',
            name='comment',
            field=models.ForeignKey(to='easypr_ng.Comment'),
        ),
        migrations.AddField(
            model_name='commentreply',
            name='posted_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
