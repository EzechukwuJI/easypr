# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('easypr_ng', '0006_auto_20161018_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket_number', models.CharField(max_length=14)),
                ('preferred_interview_date', models.DateTimeField()),
                ('interview_venue', models.TextField(max_length=300, null=True)),
                ('interview_date', models.DateTimeField()),
                ('interview_time', models.DateTimeField()),
                ('contact_person', models.CharField(max_length=125)),
                ('contact_email', models.EmailField(max_length=255)),
                ('phone_number', models.IntegerField(max_length=15)),
                ('person_to_be_interviewed', models.CharField(max_length=125)),
                ('status', models.CharField(default=b'new', max_length=25, choices=[(b'new', b'new'), (b'contacted', b'contacted'), (b'in_progress', b'In progress'), (b'closed', b'closed')])),
                ('request_outcome', models.CharField(max_length=25, choices=[(b'success', b'success'), (b'declined', b'declined'), (b'deferred', b'deferred'), (b'dropped', b'dropped')])),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('date_closed', models.DateTimeField(null=True, blank=True)),
                ('closed_by', models.OneToOneField(related_name='interview_closed_by', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('contacted_by', models.OneToOneField(related_name='interview_contacted_by', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('preferred_media_house', models.ManyToManyField(to='easypr_ng.MediaHouse')),
            ],
            options={
                'ordering': ('-date_requested',),
                'verbose_name_plural': 'Interview request',
            },
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket_number', models.CharField(max_length=14)),
                ('service_type', models.CharField(max_length=100, choices=[(b'Press Release Distribution', b'Press Release Distribution'), (b'Content Writing and Marketing', b'Content Marketing'), (b'Advertising', b'Advertising'), (b'SME Marketing', b'SME Marketing'), (b'Sales and Marketing', b'Sales and Marketing'), (b'Events Bureau', b'Events Bureau'), (b'Blogger Distribution', b'Blogger Distribution')])),
                ('sector', models.CharField(max_length=100, choices=[(b'Finance', b'Finance')])),
                ('brief_description', models.TextField(max_length=500, null=True, blank=True)),
                ('target_media', models.CharField(max_length=125, choices=[(b'Newspaper', b'Newspaper'), (b'Blog', b'Blog')])),
                ('time_service_needed', models.CharField(max_length=75)),
                ('preffered_call_time', models.CharField(max_length=50)),
                ('allow_call', models.BooleanField(default=False)),
                ('contact_person', models.CharField(max_length=125)),
                ('contact_email', models.EmailField(max_length=255)),
                ('phone_number', models.IntegerField(max_length=15)),
                ('status', models.CharField(default=b'new', max_length=25, choices=[(b'new', b'new'), (b'contacted', b'contacted'), (b'in_progress', b'In progress'), (b'closed', b'closed')])),
                ('request_outcome', models.CharField(max_length=25, choices=[(b'success', b'success'), (b'declined', b'declined'), (b'deferred', b'deferred'), (b'dropped', b'dropped')])),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('date_closed', models.DateTimeField(null=True, blank=True)),
                ('closed_by', models.OneToOneField(related_name='closed_by', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('contacted_by', models.OneToOneField(related_name='contacted_by', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_requested',),
                'verbose_name_plural': 'Service request',
            },
        ),
        migrations.AlterField(
            model_name='prstrategy',
            name='action_status',
            field=models.CharField(default=b'Contacted', max_length=75, choices=[(b'new', b'new'), (b'contacted', b'contacted'), (b'in_progress', b'In progress'), (b'closed', b'closed')]),
        ),
    ]
