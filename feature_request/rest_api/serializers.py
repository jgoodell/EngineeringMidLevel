from .models import (Client,
                     ProductArea,
                     FeatureRequest,
                     )
from rest_framework import serializers


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('name',)


class ProductAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductArea
        fields = ('name',)


class FeatureRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeatureRequest
        fields = ('title', 'description', 'client', 'client_priority',
                  'target_date', 'ticket_uri', 'product_area',)
