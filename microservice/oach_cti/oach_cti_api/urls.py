from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import CtiEvent
import django_eventstream

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('store-cti-event/', CtiEvent.as_view({
        'post': 'store',
    }), name='store-cti-event'),
    path('get-cti-event/<str:pk>', CtiEvent.as_view({
        'get': 'retrieve',
    }), name='get-cti-event'),
    # path('cti-events/<login>/messages/', views.messages),
    path('cti-events/<login>/events/', include(django_eventstream.urls), {
        'format-channels': ['cti-{login}']
    }),
]