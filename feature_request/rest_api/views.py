from .models import (Client,
                     ProductArea,
                     FeatureRequest,
                     )

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import (ClientSerializer,
                          ProductAreaSerializer,
                          FeatureRequestSerializer,
                          )


class ClientViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for client actions.
    """
    queryset = Client.objects.all().order_by('name')
    serializer_class = ClientSerializer


class ProductAreaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for product area actions.
    """
    
    queryset = ProductArea.objects.all().order_by('name')
    serializer_class = ProductAreaSerializer


class FeatureRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint for feature request actions.
    """

    queryset = FeatureRequest.objects.all().order_by('target_date')
    serializer_class = FeatureRequest
