# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browsehistory',
            name='create_time',
            field=models.DateTimeField(help_text=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='browsehistory',
            name='extinfo',
            field=jsonfield.fields.JSONField(default={}, help_text=b'\xe6\x89\xa9\xe5\xb1\x95\xe5\xad\x97\xe6\xae\xb5', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='browsehistory',
            name='goods',
            field=models.ForeignKey(help_text=b'\xe5\x95\x86\xe5\x93\x81', to='goods.Goods'),
        ),
        migrations.AlterField(
            model_name='browsehistory',
            name='update_time',
            field=models.DateTimeField(help_text=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', auto_now=True),
        ),
        migrations.AlterField(
            model_name='browsehistory',
            name='user',
            field=models.ForeignKey(help_text=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='addr_detail',
            field=models.CharField(help_text=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x9c\xb0\xe5\x9d\x80', max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(help_text=b'\xe5\xb8\x82', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='county',
            field=models.CharField(help_text=b'\xe5\x8e\xbf', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='create_time',
            field=models.DateTimeField(help_text=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='extinfo',
            field=jsonfield.fields.JSONField(default={}, help_text=b'\xe6\x89\xa9\xe5\xb1\x95\xe5\xad\x97\xe6\xae\xb5', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='province',
            field=models.CharField(help_text=b'\xe7\x9c\x81', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='realname',
            field=models.CharField(help_text=b'\xe7\x9c\x9f\xe5\xae\x9e\xe5\xa7\x93\xe5\x90\x8d', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.IntegerField(default=3, help_text=b'\xe6\x80\xa7\xe5\x88\xab'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='update_time',
            field=models.DateTimeField(help_text=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', auto_now=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.IntegerField(help_text=b'\xe7\x94\xa8\xe6\x88\xb7ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.SmallIntegerField(default=1, help_text=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
    ]
