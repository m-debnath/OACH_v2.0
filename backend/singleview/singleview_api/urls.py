from django.urls import path
from .views import AccountViewSet, ActivityViewSet, ServiceRequestViewSet, InvoiceViewSet, PaymentViewSet, TreatmentViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('accounts', AccountViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('accounts/search/', AccountViewSet.as_view({
        'get': 'search',
    })),
    path('accounts/<str:pk>', AccountViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('activities', ActivityViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('activities/search/', ActivityViewSet.as_view({
        'get': 'search',
    })),
    path('activities/<str:pk>', ActivityViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('service_requests', ServiceRequestViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('service_requests/search/', ServiceRequestViewSet.as_view({
        'get': 'search',
    })),
    path('service_requests/<str:pk>', ServiceRequestViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('invoices', InvoiceViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('invoices/search/', InvoiceViewSet.as_view({
        'get': 'search',
    })),
    path('invoices/<str:pk>', InvoiceViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('payments', PaymentViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('payments/search/', PaymentViewSet.as_view({
        'get': 'search',
    })),
    path('payments/<str:pk>', PaymentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('treatments', TreatmentViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('treatments/search/', TreatmentViewSet.as_view({
        'get': 'search',
    })),
    path('treatments/<str:pk>', TreatmentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
