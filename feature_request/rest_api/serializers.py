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
    title = serializers.CharField(required=True, allow_blank=False,
                                  max_length=128)
    description = serializers.CharField(required=True, allow_blank=False,
                                        max_length=512)
    client_uri = serializers.HyperlinkedIdentityField(
        view_name='client', format='html')
    client_priority = serializers.IntegerField(read_only=False)
    target_date = serializers.DateTimeField()
    ticket_uri = serializers.CharField(required=True, allow_blank=False,
                                       max_length=256)
    product_area_uri = serializers.HyperlinkedIdentityField(
        view_name='product-area', format='html')
 

    def create(self, validated_data):
        return FeatureRequest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.client_uri = validated_data.get('client_uri',
                                                 instance.client_uri)
        instance.client_priority = validated_data.get('client_priority',
                                                      instance.priority)
        instance.target_date = validated_data.get('target_date',
                                                  instance.target_date)
        instance.ticket_uri = validated_data.get('ticket_uri',
                                                 instance.ticket_uri)
        instance.product_area_uri = validated_data.get(
            'product_area_uri',
            instance.product_area_uri)
        instance.save()
        return instance
    
    class Meta:
        model = FeatureRequest
        fields = ('title', 'description', 'client_uri',
                  'client_priority', 'target_date', 'ticket_uri',
                  'product_area_uri',)
