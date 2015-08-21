# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('client_priority', models.IntegerField(verbose_name=b'client priority')),
                ('target_date', models.DateTimeField(verbose_name=b'target date')),
                ('ticket_uri', models.CharField(max_length=256)),
            ],
        ),
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
        migrations.RenameModel(
            old_name='ProductAreas',
            new_name='ProductArea',
        ),
        migrations.RemoveField(
            model_name='featurerequests',
            name='ProductArea',
        ),
        migrations.RemoveField(
            model_name='featurerequests',
            name='client',
        ),
        migrations.DeleteModel(
            name='FeatureRequests',
        ),
        migrations.AddField(
            model_name='featurerequest',
            name='client',
            field=models.ForeignKey(to='rest_api.Client'),
        ),
        migrations.AddField(
            model_name='featurerequest',
            name='product_area',
            field=models.ForeignKey(to='rest_api.ProductArea'),
        ),
    ]
