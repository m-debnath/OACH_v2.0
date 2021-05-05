from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ActivitiesList, ActivityDetails

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('get-activities-by-account-id/<str:pk>', ActivitiesList.as_view({
        'get': 'retrieve',
    }), name='get-activities-by-account-id'),
    path('create-activity', ActivityDetails.as_view({
        'post': 'create',
    }), name='create-activity'),
    path('update-activity-by-id/<str:pk>', ActivityDetails.as_view({
        'post': 'update',
    }), name='update-activity-by-id'),
]
