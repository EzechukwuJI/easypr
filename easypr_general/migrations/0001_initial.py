# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField(max_length=300, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=20, null=True, choices=[(b'Nigeria', b'Nigeria'), (b'Ghana', b'Ghana'), (b'Kenya', b'Kenya')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
        migrations.CreateModel(
            name='ClientFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(max_length=125)),
                ('email', models.CharField(max_length=225)),
                ('subject', models.CharField(max_length=225)),
                ('message', models.TextField(max_length=1000)),
                ('date_sent', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default=b'Open', max_length=20, choices=[(b'Open', b'Open'), (b'Closed', b'Closed'), (b'Pending', b'Pending')])),
            ],
        ),
        migrations.CreateModel(
            name='LatestNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=200)),
                ('news_content', models.CharField(max_length=300)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PwResetRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reset_code', models.CharField(max_length=50)),
                ('expired', models.BooleanField(default=False)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=15, choices=[(b'Mr', b'Mr'), (b'Mrs', b'Mrs'), (b'Dr', b'Dr')])),
                ('account_type', models.CharField(max_length=20)),
                ('phone_no', models.CharField(max_length=15)),
                ('company_name', models.CharField(max_length=100, null=True, blank=True)),
                ('economy_sector', models.CharField(max_length=75)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('profile_upto_date', models.BooleanField(default=False)),
                ('website', models.CharField(max_length=175, null=True)),
                ('brand_logo', models.ImageField(upload_to=b'Client/logo/%Y-%M-%D')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('registration_code', models.CharField(max_length=50)),
                ('address', models.ForeignKey(default=None, to='easypr_general.Address', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
