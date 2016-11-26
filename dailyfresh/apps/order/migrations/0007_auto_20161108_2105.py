# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20161027_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorder',
            name='addr',
            field=models.ForeignKey(help_text=b'\xe5\x9c\xb0\xe5\x9d\x80', to='address.Address'),
        ),
        migrations.AlterField(
            model_name='sorder',
            name='create_time',
            field=models.DateTimeField(help_text=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sorder',
            name='ex_price',
            field=models.FloatField(default=10.0, help_text=b'\xe5\x95\x86\xe5\x93\x81\xe8\xbf\x90\xe8\xb4\xb9'),
        ),
        migrations.AlterField(
            model_name='sorder',
            name='extinfo',
            field=jsonfield.fields.JSONField(default={}, help_text=b'\xe6\x89\xa9\xe5\xb1\x95\xe5\xad\x97\xe6\xae\xb5', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sorder',
            name='order_status',
            field=models.SmallIntegerField(default=1, help_text=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='sorder',
            name='payment_method',
            field=models.SmallIntegerField(default=1, help_text=b'\xe6\x94\xaf\xe4\xbb\x98\xe6\x96\xb9\xe5\xbc\x8f'),
        ),
        migrations.AlterField(
            model_name='sorder',
            name='total_amount',
            field=models.FloatField(default=0.0, help_text=b'\xe8\xae\xa2\xe5\x8d\x95\xe6\x80\xbb\xe9\xa2\x9d'),
        ),
        migrations.AlterField(
            model_name='sorder',
            name='total_count',
            field=models.SmallIntegerField(default=1, help_text=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x95\x86\xe5\x93\x81\xe6\x95\xb0\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='sorder',
            name='update_time',
            field=models.DateTimeField(help_text=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', auto_now=True),
        ),
        migrations.AlterField(
            model_name='sorder',
            name='user',
            field=models.ForeignKey(help_text=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sordergoods',
            name='comment',
            field=models.TextField(default=b'', help_text=b'\xe5\x95\x86\xe5\x93\x81\xe8\xaf\x84\xe4\xbb\xb7'),
        ),
        migrations.AlterField(
            model_name='sordergoods',
            name='create_time',
            field=models.DateTimeField(help_text=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sordergoods',
            name='extinfo',
            field=jsonfield.fields.JSONField(default={}, help_text=b'\xe6\x89\xa9\xe5\xb1\x95\xe5\xad\x97\xe6\xae\xb5', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sordergoods',
            name='goods',
            field=models.ForeignKey(help_text=b'\xe5\x95\x86\xe5\x93\x81', to='goods.Goods'),
        ),
        migrations.AlterField(
            model_name='sordergoods',
            name='goods_count',
            field=models.SmallIntegerField(default=1, help_text=b'\xe5\x95\x86\xe5\x93\x81\xe6\x95\xb0\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='sordergoods',
            name='goods_price',
            field=models.FloatField(default=0.0, help_text=b'\xe5\x95\x86\xe5\x93\x81\xe5\x8d\x95\xe4\xbb\xb7'),
        ),
        migrations.AlterField(
            model_name='sordergoods',
            name='sorder',
            field=models.ForeignKey(help_text=b'\xe8\xae\xa2\xe5\x8d\x95', to='order.SOrder'),
        ),
        migrations.AlterField(
            model_name='sordergoods',
            name='update_time',
            field=models.DateTimeField(help_text=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', auto_now=True),
        ),
    ]
