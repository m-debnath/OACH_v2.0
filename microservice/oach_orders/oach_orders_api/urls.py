from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import OrdersList

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('get-orders-by-account-id/<str:pk>', OrdersList.as_view({
        'get': 'retrieve',
    }), name='get-order-by-account-id'),
]
