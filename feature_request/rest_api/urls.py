from django.conf.urls import (url,
                              include,
                              )
from rest_framework import routers
import views


router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'product-areas', views.ProductAreaViewSet)
router.register(r'feature-requests', views.FeatureRequestViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
    ]
