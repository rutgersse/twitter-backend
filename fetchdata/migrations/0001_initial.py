# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coordinates', models.CharField(max_length=255, null=True, blank=True)),
                ('created_at', models.CharField(max_length=255, null=True, blank=True)),
                ('entities', models.CharField(max_length=255, null=True, blank=True)),
                ('geo', models.CharField(max_length=255, null=True, blank=True)),
                ('tweet_id', models.CharField(max_length=255, null=True, blank=True)),
                ('id_str', models.CharField(max_length=255, null=True, blank=True)),
                ('lang', models.CharField(max_length=255, null=True, blank=True)),
                ('meta', models.CharField(max_length=255, null=True, blank=True)),
                ('place', models.CharField(max_length=255, null=True, blank=True)),
                ('tweet', models.CharField(max_length=255, null=True, blank=True)),
                ('user_created_at', models.CharField(max_length=255, null=True, blank=True)),
                ('geo_enabled', models.CharField(max_length=255, null=True, blank=True)),
                ('user_id', models.CharField(max_length=255, null=True, blank=True)),
                ('user_id_str', models.CharField(max_length=255, null=True, blank=True)),
                ('user_lang', models.CharField(max_length=255, null=True, blank=True)),
                ('user_location', models.CharField(max_length=255, null=True, blank=True)),
                ('user_name', models.CharField(max_length=255, null=True, blank=True)),
                ('user_screen_name', models.CharField(max_length=255, null=True, blank=True)),
                ('user_timezone', models.CharField(max_length=255, null=True, blank=True)),
                ('processed', models.IntegerField(default=0)),
            ],
        ),
    ]
