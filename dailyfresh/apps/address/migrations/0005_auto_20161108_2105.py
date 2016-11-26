# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_auto_20161024_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='addr_detail',
            field=models.CharField(help_text=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x9c\xb0\xe5\x9d\x80', max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(help_text=b'\xe5\xb8\x82', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='county',
            field=models.CharField(help_text=b'\xe5\x8e\xbf', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='create_time',
            field=models.DateTimeField(help_text=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='extinfo',
            field=jsonfield.fields.JSONField(default={}, help_text=b'\xe6\x89\xa9\xe5\xb1\x95\xe5\xad\x97\xe6\xae\xb5', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='province',
            field=models.CharField(help_text=b'\xe7\x9c\x81', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='recipient_name',
            field=models.CharField(help_text=b'\xe6\x94\xb6\xe4\xbb\xb6\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='recipient_phone',
            field=models.CharField(help_text=b'\xe6\x94\xb6\xe4\xbb\xb6\xe4\xba\xba\xe7\x94\xb5\xe8\xaf\x9d', max_length=11, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='update_time',
            field=models.DateTimeField(help_text=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', auto_now=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(help_text=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(help_text=b'\xe9\x82\xae\xe7\xbc\x96', max_length=10, null=True, blank=True),
        ),
    ]
