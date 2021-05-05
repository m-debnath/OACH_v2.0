from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import AccountDetails, AccountHierarchyDetails

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('get-account-by-id/<str:pk>', AccountDetails.as_view({
        'get': 'retrieve',
    }), name='get-account-by-id'),
    path('search-by-account-number/<str:pk>', AccountDetails.as_view({
        'get': 'search',
    }), name='search-by-account-number'),
    path('upd-account-by-id/<str:pk>', AccountDetails.as_view({
        'post': 'update',
    }), name='upd-account-by-id'),
    path('get-account-hier-by-id/<str:pk>', AccountHierarchyDetails.as_view({
        'get': 'retrieve',
    }), name='get-account-hier-by-id'),
]
