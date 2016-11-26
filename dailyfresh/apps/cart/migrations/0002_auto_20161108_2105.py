# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='create_time',
            field=models.DateTimeField(help_text=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='extinfo',
            field=jsonfield.fields.JSONField(default={}, help_text=b'\xe6\x89\xa9\xe5\xb1\x95\xe5\xad\x97\xe6\xae\xb5', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(help_text=b'\xe5\x95\x86\xe5\x93\x81', to='goods.Goods'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='goods_num',
            field=models.SmallIntegerField(default=1, help_text=b'\xe5\x95\x86\xe5\x93\x81\xe6\x95\xb0\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='update_time',
            field=models.DateTimeField(help_text=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', auto_now=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(help_text=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
    ]
