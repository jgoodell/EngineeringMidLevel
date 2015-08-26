from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=128)


class ProductArea(models.Model):
    name = models.CharField(max_length=128)


class FeatureRequest(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    client_uri = models.CharField('client uri', max_length=256,
                                  default='')
    client_priority = models.IntegerField('client priority')
    target_date = models.DateTimeField('target date')
    ticket_uri = models.CharField('ticket uri', max_length=256)
    product_area_uri = models.CharField('product area uri',
                                        max_length=256,
                                        default='')

