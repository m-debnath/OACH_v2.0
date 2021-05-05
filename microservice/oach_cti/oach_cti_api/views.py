from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from django_eventstream import send_event
import json

class CtiEvent(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def store(self, request):
        key = request.data.get('login', '')
        cache.set(key, json.dumps(request.data))
        send_event('cti-{}'.format(key), 'message', json.loads(cache.get(key)))
        return Response(json.loads(cache.get(key)), status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        print(pk)
        if cache.get(pk) == None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(json.loads(cache.get(pk)), status=status.HTTP_200_OK)