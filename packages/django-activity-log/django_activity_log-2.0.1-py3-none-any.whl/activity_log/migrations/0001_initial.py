# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='user id ')),
                ('user', models.CharField(max_length=256, verbose_name='user')),
                ('request_url', models.CharField(max_length=256, verbose_name='url')),
                ('request_method', models.CharField(db_index=True, max_length=10, verbose_name='http method')),
                ('response_code', models.CharField(db_index=True, max_length=3, verbose_name='response code')),
                ('datetime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='datetime')),
                ('extra_data', models.TextField(blank=True, null=True, verbose_name='extra data')),
                ('ip_address', models.GenericIPAddressField(blank=True, db_index=True, null=True, verbose_name='user IP')),
                ('headers', models.TextField(blank=True, null=True)),
                ('payload', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'activity log',
            },
        ),
        migrations.CreateModel(
            name='BlackListIPAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('block_network_address', models.BooleanField(default=False)),
                ('blocked' , models.BooleanField(default = True))
            ],
            options={
                'verbose_name': 'blocked ip',
                'verbose_name_plural': 'blocked ips',
            },
        ),
    ]

