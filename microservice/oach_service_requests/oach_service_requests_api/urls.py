from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ServiceRequestsList, ServiceRequestDetails

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('get-service-requests-by-account-id/<str:pk>', ServiceRequestsList.as_view({
        'get': 'retrieve',
    }), name='get-service-requests-by-account-id'),
    path('create-service-request', ServiceRequestDetails.as_view({
        'post': 'create',
    }), name='create-service-request'),
    path('update-service-request-by-id/<str:pk>', ServiceRequestDetails.as_view({
        'post': 'update',
    }), name='update-service-request-by-id'),
]
