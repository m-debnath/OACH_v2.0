from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import AssetList, AssetPAVList

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('get-asset-by-account-id/<str:pk>', AssetList.as_view({
        'get': 'retrieve',
    }), name='get-asset-by-account-id'),
    path('get-asset-by-pav/<str:pk>', AssetPAVList.as_view({
        'get': 'retrieve',
    }), name='get-asset-by-pav'),
]
