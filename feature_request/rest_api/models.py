from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=128)


class ProductArea(models.Model):
    name = models.CharField(max_length=128)


class FeatureRequest(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    client = models.ForeignKey(Client)
    client_priority = models.IntegerField('client priority')
    target_date = models.DateTimeField('target date')
    ticket_uri = models.CharField(max_length=256)
    product_area = models.ForeignKey(ProductArea)

