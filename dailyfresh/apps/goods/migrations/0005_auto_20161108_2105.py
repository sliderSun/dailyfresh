# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20161027_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(help_text=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='extinfo',
            field=jsonfield.fields.JSONField(default={}, help_text=b'\xe6\x89\xa9\xe5\xb1\x95\xe5\xad\x97\xe6\xae\xb5', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_ex_price',
            field=models.FloatField(default=0.0, help_text=b'\xe5\x95\x86\xe5\x93\x81\xe8\xbf\x90\xe8\xb4\xb9'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_info',
            field=models.TextField(help_text=b'\xe5\x95\x86\xe5\x93\x81\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_name',
            field=models.CharField(default=b'', help_text=b'\xe5\x95\x86\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0', max_length=64),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_price',
            field=models.FloatField(default=0.0, help_text=b'\xe5\x95\x86\xe5\x93\x81\xe4\xbb\xb7\xe6\xa0\xbc'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_sales',
            field=models.IntegerField(default=1, help_text=b'\xe5\x95\x86\xe5\x93\x81\xe9\x94\x80\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_status',
            field=models.IntegerField(default=1, help_text=b'\xe5\x95\x86\xe5\x93\x81\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_stock',
            field=models.IntegerField(default=1, help_text=b'\xe5\x95\x86\xe5\x93\x81\xe5\xba\x93\xe5\xad\x98'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_subtitle',
            field=models.CharField(default=b'', help_text=b'\xe5\x95\x86\xe5\x93\x81\xe5\x89\xaf\xe6\xa0\x87\xe9\xa2\x98', max_length=128),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_type_id',
            field=models.SmallIntegerField(default=1, help_text=b'\xe5\x95\x86\xe5\x93\x81\xe5\x88\x86\xe7\xb1\xbbID'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_unit',
            field=models.IntegerField(default=1, help_text=b'\xe5\x95\x86\xe5\x93\x81\xe5\x8d\x95\xe4\xbd\x8d'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='update_time',
            field=models.DateTimeField(help_text=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', auto_now=True),
        ),
    ]
