from django.urls import path
from .views import OrderViewSet, OrderItemViewSet, InstalledAssetViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('orders', OrderViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('orders/search/', OrderViewSet.as_view({
        'get': 'search',
    })),
    path('orders/<str:pk>', OrderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('order_items', OrderItemViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('order_items/search/', OrderItemViewSet.as_view({
        'get': 'search',
    })),
    path('order_items/<str:pk>', OrderItemViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('assets', InstalledAssetViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('assets/search/', InstalledAssetViewSet.as_view({
        'get': 'search',
    })),
    path('assets/<str:pk>', InstalledAssetViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
