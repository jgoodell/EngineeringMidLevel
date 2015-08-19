from django.db import models


class Clients(models.Model):
    name = models.CharField(max_length=128)


class ProductAreas(models.Model):
    name = models.CharField(max_length=128)


class FeatureRequests(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    client = models.ForeignKey(Clients)
    client_priority = models.IntegerField('client priority')
    target_date = models.DateTimeField('target date')
    ticket_uri = models.CharField(max_length=256)
    ProductArea = models.ForeignKey(ProductAreas)

