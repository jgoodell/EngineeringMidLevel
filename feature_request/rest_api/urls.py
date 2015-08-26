from django.conf.urls import (url,
                              include,
                              )
#from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
import views


#router = routers.DefaultRouter()
#router.register(r'clients', views.ClientViewSet)
#router.register(r'product-areas', views.ProductAreaViewSet)
#router.register(r'feature-requests', views.FeatureRequestViewSet)
#urlpatterns = [
#    url(r'^', include(router.urls)),
#    url(r'^$', views.api_root)
#    ]

urlpatterns = format_suffix_patterns([
    url(r'^clients/$',
        views.ClientListView.as_view(),
        name='clients'),
    url(r'^clients/(?P<pk>[0-9]+)/$',
        views.ClientView.as_view(),
        name='client'),
    url(r'^product-areas/$',
        views.ProductAreaListView.as_view(),
        name='product_areas'),
    url(r'^product-areas/(?P<pk>[0-9]+)/$',
        views.ProductAreaView.as_view(),
        name='product_area'),
    url(r'^feature-requests/$',
        views.FeatureRequestListView.as_view(),
        name='feature_requests'),
    url(r'^feature-requests/(?P<pk>[0-9]+)/$',
        views.FeatureRequestView.as_view(),
        name='feature_request')
    ])


urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
    ]
