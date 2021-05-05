from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import InvoicesList

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('get-invoices-by-billingaccount-id/<str:pk>', InvoicesList.as_view({
        'get': 'retrieve',
    }), name='get-invoices-by-billingaccount-id'),
]
