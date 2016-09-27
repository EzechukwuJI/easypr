# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0002_remove_mediahouse_contact_persons'),
    ]

    operations = [
        migrations.CreateModel(
            name='PRStrategy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annonymous_user_id', models.CharField(max_length=75)),
                ('business_type', models.CharField(default=b'Company', max_length=25, choices=[(b'Company', b'Company'), (b'Individual', b'Individual')])),
                ('company_type', models.CharField(default=b'Private', max_length=75, choices=[(b'Public', b'Public'), (b'Private', b'Private')])),
                ('is_pr_agent', models.CharField(default=b'No', max_length=75, choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('size_of_pr_team', models.IntegerField(default=0)),
                ('target_audience', models.TextField(max_length=1000, null=True)),
                ('pr_goals', models.TextField(max_length=1000, null=True)),
                ('frequency_of_pr', models.CharField(default=b'monthly', max_length=100, choices=[(b'monthly', b'Monthly'), (b'annually', b'Annually'), (b'quartely', b'Quartely'), (b'several-times-a-month', b'Several Times a Month'), (b'first-time-user', b'first-time-user'), (b'first-time-user', b'first-time-user'), (b'weekly', b'Weekly')])),
                ('target_audience_location', models.CharField(max_length=125, null=True)),
                ('currently_use_pr_db', models.BooleanField(default=False)),
                ('social_media_used', models.TextField(max_length=1000, null=True)),
                ('pr_db_used', models.TextField(max_length=1000, null=True)),
                ('require_pr_writing', models.BooleanField(default=False)),
                ('require_media_pitching', models.BooleanField(default=False)),
                ('do_you_have_newsroom', models.BooleanField(default=False)),
                ('name_pr_newsroom_link', models.CharField(max_length=200)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('action_status', models.CharField(default=b'Contacted', max_length=75, choices=[(b'contacted', b'contacted'), (b'closed', b'closed')])),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('contact_name', models.CharField(max_length=125, null=True)),
                ('email', models.CharField(max_length=125, null=True)),
                ('phone_number', models.CharField(max_length=25, null=True)),
            ],
            options={
                'ordering': ['date_submitted'],
                'verbose_name_plural': 'PR Strategy',
            },
        ),
    ]
