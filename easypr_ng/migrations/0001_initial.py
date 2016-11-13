# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(max_length=1000)),
                ('website', models.CharField(max_length=150, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('reply', models.TextField(max_length=1000)),
                ('comment', models.ForeignKey(to='easypr_ng.Comment')),
                ('posted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket_number', models.CharField(max_length=14)),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('date_closed', models.DateTimeField()),
                ('status', models.CharField(default=b'new', max_length=25, choices=[(b'new', b'new'), (b'contacted', b'contacted'), (b'in_progress', b'In progress'), (b'closed', b'closed')])),
                ('request_outcome', models.CharField(default=b'pending', max_length=25, choices=[(b'pending', b'pending'), (b'success', b'success'), (b'declined', b'declined'), (b'deferred', b'deferred'), (b'dropped', b'dropped')])),
                ('contact_person', models.CharField(max_length=125)),
                ('contact_email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('preferred_interview_date', models.DateTimeField()),
                ('interview_venue', models.TextField(max_length=300, null=True)),
                ('interview_date', models.DateTimeField()),
                ('interview_time', models.DateTimeField()),
                ('person_to_be_interviewed', models.CharField(max_length=125)),
                ('closed_by', models.OneToOneField(related_name='interview_closed_by', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('contacted_by', models.OneToOneField(related_name='interview_contacted_by', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_requested',),
                'verbose_name_plural': 'Interview request',
            },
        ),
        migrations.CreateModel(
            name='MediaContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=125)),
                ('last_name', models.CharField(max_length=125)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=225)),
                ('phone_number', models.CharField(max_length=15, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaHouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('name_slug', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaPlatform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('name_slug', models.CharField(max_length=75)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, choices=[(b'basic', b'Basic'), (b'regular', b'Regular'), (b'premium', b'Premium'), (b'premium-plus', b'Premium Plus')])),
                ('media_outreach_credit', models.CharField(default=1, max_length=25)),
                ('online', models.CharField(max_length=5, verbose_name=b'online_newspaper_publishing', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('monitoring', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('free_consulting', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('newsroom', models.CharField(max_length=5, verbose_name=b'Newsroom via EasyPR Media Desk', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('google_news_inclusions', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('reuters_news_network', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('hyperlinks', models.CharField(max_length=5, verbose_name=b'hyperlinks in online press release')),
                ('notification', models.CharField(max_length=5, verbose_name=b'publication notification via email', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('autopost', models.CharField(max_length=5, verbose_name=b'autopost to social media account', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('analytics', models.CharField(max_length=5, verbose_name=b'detailed analytics report', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('expedited', models.CharField(max_length=5, verbose_name=b'expedited release processing', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('available_on_homepage', models.CharField(max_length=5, verbose_name=b'news made available to journalists, bloggers and researchers via EasyPR homepage', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('content_writing', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('content_editing', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('featured_package', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('price_naira', models.FloatField(default=0.0, max_length=25)),
                ('price_dollar', models.FloatField(default=0.0, max_length=25)),
                ('active', models.BooleanField(default=False)),
                ('is_promo', models.BooleanField(default=False)),
                ('promo_starts', models.DateTimeField(auto_now_add=True)),
                ('promo_ends', models.DateTimeField(auto_now_add=True)),
                ('promo_price_dollar', models.FloatField(default=0.0, max_length=25)),
                ('promo_price_naira', models.FloatField(default=0.0, max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.CreateModel(
            name='PayDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.CharField(max_length=25, null=True)),
                ('payment_method', models.CharField(default=b'', max_length=75, choices=[(b'Bank Deposit', b'Bank Deposit'), (b'Card Payment', b'Card Payment'), (b'Bank Transfer', b'Bank Transfer')])),
                ('amount_paid', models.FloatField(default=0.0)),
                ('date_paid', models.CharField(max_length=100, null=True, blank=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True, choices=[(b'Diamond Bank', b'Diamond Bank'), (b'GTB', b'GTB')])),
                ('currency', models.CharField(max_length=100, null=True, blank=True)),
                ('teller_number', models.CharField(max_length=15, null=True, blank=True)),
                ('pay_status', models.CharField(default=b'pending', max_length=25, choices=[(b'verified', b'verified'), (b'pending', b'pending'), (b'failed', b'failed')])),
                ('verified_by', models.BooleanField(default=False)),
                ('date_verified', models.DateTimeField(null=True, blank=True)),
                ('user', models.ForeignKey(verbose_name=b'Payment By', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PressMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_slug', models.CharField(max_length=150)),
                ('media_type', models.CharField(max_length=150)),
                ('price_per', models.FloatField(default=0.0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('caption', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='PRStrategy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anon_userID', models.CharField(max_length=75, verbose_name=b'Annonymous user ID')),
                ('business_type', models.CharField(default=b'Company', max_length=25, choices=[(b'NA', b'NA'), (b'Company', b'Company'), (b'Individual', b'Individual')])),
                ('company_type', models.CharField(default=b'Private', max_length=75, choices=[(b'NA', b'NA'), (b'Public', b'Public'), (b'Private', b'Private')])),
                ('is_pr_agent', models.CharField(default=b'No', max_length=75, choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('size_of_pr_team', models.IntegerField(default=0)),
                ('target_audience', models.TextField(max_length=1000, null=True)),
                ('pr_goals', models.TextField(max_length=1000, null=True)),
                ('frequency_of_pr', models.CharField(default=b'monthly', max_length=100, choices=[(b'NA', b'NA'), (b'weekly', b'Weekly'), (b'monthly', b'Monthly'), (b'several-times-a-month', b'Several Times a Month'), (b'quartely', b'Quartely'), (b'annually', b'Annually'), (b'first-time-user', b'First Time User')])),
                ('target_audience_location', models.CharField(max_length=250, null=True)),
                ('currently_use_pr_db', models.BooleanField(default=False)),
                ('social_media_used', models.TextField(max_length=1000, null=True)),
                ('pr_db_used', models.TextField(max_length=1000, null=True)),
                ('require_pr_writing', models.BooleanField(default=False)),
                ('require_media_pitching', models.BooleanField(default=False)),
                ('do_you_have_newsroom', models.BooleanField(default=False)),
                ('name_pr_newsroom_link', models.CharField(max_length=200)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('action_status', models.CharField(default=b'Contacted', max_length=75, choices=[(b'new', b'new'), (b'contacted', b'contacted'), (b'in_progress', b'In progress'), (b'closed', b'closed')])),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('contact_name', models.CharField(max_length=125, null=True)),
                ('email', models.CharField(max_length=125, null=True)),
                ('phone_number', models.CharField(max_length=25, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['date_submitted'],
                'verbose_name_plural': 'PR Strategy',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.CharField(max_length=15)),
                ('post_title', models.CharField(max_length=175)),
                ('title_slug', models.CharField(max_length=200)),
                ('status', models.CharField(default=b'New', max_length=50, choices=[(b'New', b'New'), (b'sent_to_external_editor', b'sent_to_external_editor'), (b'Processing', b'Processing'), (b'Published', b'Published'), (b'Rejected', b'Rejected')])),
                ('post_body', models.TextField(max_length=3000, null=True, blank=True)),
                ('person_to_quote', models.CharField(max_length=125, null=True, blank=True)),
                ('persons_position', models.CharField(max_length=125, null=True, blank=True)),
                ('uploaded_text', models.FileField(null=True, upload_to=b'publication/%Y-%M-%D', blank=True)),
                ('date_published', models.DateTimeField(null=True, blank=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('publish_online', models.BooleanField(default=False, verbose_name=b'Do you also want online publication of the chosen media? ')),
                ('completed', models.BooleanField(default=False)),
                ('assigned_to', models.ForeignKey(related_name='Third_party_Editor', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('media_houses', models.ManyToManyField(to='easypr_ng.MediaHouse')),
                ('platform', models.ForeignKey(verbose_name=b'Media platform', blank=True, to='easypr_ng.MediaPlatform', null=True)),
                ('posted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('press_material', models.ForeignKey(verbose_name=b'Media category', blank=True, to='easypr_ng.PressMaterial', null=True)),
                ('published_by', models.ForeignKey(related_name='Edited_and_published_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublicationImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(null=True, upload_to=b'publicaton_image/%Y/%M/%D', blank=True)),
                ('caption', models.CharField(max_length=200, null=True, blank=True)),
                ('post', models.ForeignKey(blank=True, to='easypr_ng.Publication', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.CharField(max_length=15)),
                ('deleted', models.BooleanField(default=False)),
                ('ordered', models.BooleanField(default=False)),
                ('status', models.CharField(default=b'New', max_length=75, choices=[(b'New', b'New'), (b'Processing', b'Processing'), (b'Pending', b'Pending'), (b'Rejected', b'Rejected'), (b'Closed', b'Closed')])),
                ('date_purchased', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Redirect_url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('post', models.ForeignKey(blank=True, to='easypr_ng.Publication', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('name_slug', models.CharField(max_length=75)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket_number', models.CharField(max_length=14)),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('date_closed', models.DateTimeField()),
                ('status', models.CharField(default=b'new', max_length=25, choices=[(b'new', b'new'), (b'contacted', b'contacted'), (b'in_progress', b'In progress'), (b'closed', b'closed')])),
                ('request_outcome', models.CharField(default=b'pending', max_length=25, choices=[(b'pending', b'pending'), (b'success', b'success'), (b'declined', b'declined'), (b'deferred', b'deferred'), (b'dropped', b'dropped')])),
                ('contact_person', models.CharField(max_length=125)),
                ('contact_email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('service_type', models.CharField(max_length=100, choices=[(b'Press Release Distribution', b'Press Release Distribution'), (b'Content Writing and Marketing', b'Content Marketing'), (b'Advertising', b'Advertising'), (b'SME Marketing', b'SME Marketing'), (b'Sales and Marketing', b'Sales and Marketing'), (b'Events Bureau', b'Events Bureau'), (b'Blogger Distribution', b'Blogger Distribution')])),
                ('sector', models.CharField(max_length=100, choices=[(b'Finance', b'Finance')])),
                ('brief_description', models.TextField(max_length=500, null=True, blank=True)),
                ('target_media', models.CharField(max_length=125, choices=[(b'Newspaper', b'Newspaper'), (b'Blog', b'Blog')])),
                ('time_service_needed', models.CharField(max_length=75)),
                ('preferred_call_time', models.CharField(max_length=50)),
                ('allow_call', models.BooleanField(default=False)),
                ('closed_by', models.OneToOneField(related_name='closed_by', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('contacted_by', models.OneToOneField(related_name='contacted_by', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_requested',),
                'verbose_name_plural': 'Service request',
            },
        ),
        migrations.CreateModel(
            name='PurchaseInvoice',
            fields=[
                ('purchase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='easypr_ng.Purchase')),
                ('receipt_no', models.CharField(max_length=12)),
                ('invoice', models.FileField(null=True, upload_to=b'Invoices/%Y-%M-%D', blank=True)),
            ],
            bases=('easypr_ng.purchase',),
        ),
        migrations.AddField(
            model_name='purchase',
            name='package',
            field=models.ForeignKey(to='easypr_ng.Package'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='payment_details',
            field=models.ForeignKey(default=None, verbose_name=b'Payment details', to='easypr_ng.PayDetails'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='publication',
            field=models.OneToOneField(to='easypr_ng.Publication'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(verbose_name=b'Purchased By', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publication',
            name='sector',
            field=models.ForeignKey(verbose_name=b'Media sector', blank=True, to='easypr_ng.Sector', null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='site',
            field=models.ManyToManyField(to='sites.Site'),
        ),
        migrations.AddField(
            model_name='package',
            name='category',
            field=models.ForeignKey(to='easypr_ng.PressMaterial'),
        ),
        migrations.AddField(
            model_name='mediahouse',
            name='platform',
            field=models.ManyToManyField(to='easypr_ng.MediaPlatform'),
        ),
        migrations.AddField(
            model_name='mediacontact',
            name='media_house',
            field=models.ForeignKey(to='easypr_ng.MediaHouse'),
        ),
        migrations.AddField(
            model_name='interviewrequest',
            name='preferred_media_house',
            field=models.ManyToManyField(to='easypr_ng.MediaHouse'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='easypr_ng.Publication'),
        ),
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
