from django.urls import path
from .views import index, login, logout

urlpatterns = [
    path('', index, name='oach-home'),
    path('login', login, name='oach-login'),
    path('logout', logout, name='oach-logout'),
]