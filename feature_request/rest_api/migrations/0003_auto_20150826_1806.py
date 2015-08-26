# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_auto_20150821_0746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featurerequest',
            name='client',
        ),
        migrations.RemoveField(
            model_name='featurerequest',
            name='product_area',
        ),
        migrations.AddField(
            model_name='featurerequest',
            name='client_uri',
            field=models.CharField(default=b'', max_length=256, verbose_name=b'client uri'),
        ),
        migrations.AddField(
            model_name='featurerequest',
            name='product_area_uri',
            field=models.CharField(default=b'', max_length=256, verbose_name=b'product area uri'),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='ticket_uri',
            field=models.CharField(max_length=256, verbose_name=b'ticket uri'),
        ),
    ]
