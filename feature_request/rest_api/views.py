from .models import (Client,
                     ProductArea,
                     FeatureRequest,
                     )

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (ClientSerializer,
                          ProductAreaSerializer,
                          FeatureRequestSerializer,
                          )


class ClientListView(APIView):
    """
    List of all clients.
    """
    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


class ClientView(APIView):
    """
    Show client resource.
    """
    def get(self, request, format=None):
        client = Client.objects.get(pk=request.data['pk'])
        serializer = ClientSerializer(client, many=False)
        return Response(serializer.data)


class ProductAreaListView(APIView):
    """
    List of all product areas.
    """
    def get(self, request, format=None):
        product_areas = ProductArea.objects.all()
        serializer = ProductAreaSerializer(product_areas, many=True)
        return Response(serializer.data)


class ProductAreaView(APIView):
    """
    Show product area resource.
    """
    def get(self, request, format=None):
        product_area = ProductArea.objects.get(pk=request.data['pk'])
        serializer = ProductAreaSerializer(product_area, many=False)
        return Response(serializer.data)


class FeatureRequestListView(APIView):
    """
    List of all feature requests, and create new feature requests.
    """
    def get(self, request, format=None):
        feature_requests = FeatureRequest.objects.all()
        context = {'request':request}
        serializer = FeatureRequestSerializer(feature_requests,
                                              many=True,
                                              context=context)
        return Response(serializer.data)

    def post(self, request, format=None):
        context = {'request':request}
        serializer = FeatureRequestSerializer(data=request.data,
                                              context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    

class FeatureRequestView(APIView):
    """
    Show feature request resource.
    """
    def get(self, request, format=None):
        feature_request = FeatureRequest.objects.get(
            pk=request.data['pk'])
        serializer = FeatureRequestSerializer(feature_request, many=False)
        return Response(serializer.data)


#class ClientViewSet(viewsets.ReadOnlyModelViewSet):
#    """
#    API endpoint for client actions.
#    """
#    queryset = Client.objects.all().order_by('name')
#    serializer_class = ClientSerializer
#
#
#class ProductAreaViewSet(viewsets.ReadOnlyModelViewSet):
#    """
#    API endpoint for product area actions.
#    """
#    
#    queryset = ProductArea.objects.all().order_by('name')
#    serializer_class = ProductAreaSerializer
#
#
#class FeatureRequestViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint for feature request actions.
#    """
#
#    queryset = FeatureRequest.objects.all().order_by('target_date')
#    serializer_class = FeatureRequest
