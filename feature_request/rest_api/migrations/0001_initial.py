# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='FeatureRequests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('client_priority', models.IntegerField(verbose_name=b'client priority')),
                ('target_date', models.DateTimeField(verbose_name=b'target date')),
                ('ticket_uri', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAreas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='featurerequests',
            name='ProductArea',
            field=models.ForeignKey(to='rest_api.ProductAreas'),
        ),
        migrations.AddField(
            model_name='featurerequests',
            name='client',
            field=models.ForeignKey(to='rest_api.Clients'),
        ),
    ]
