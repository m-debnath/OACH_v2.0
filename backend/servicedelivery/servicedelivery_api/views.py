from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import FieldError
from .models import Order, OrderItem, InstalledAsset
from .serializers import OrderSerializer, OrderItemSerializer, InstalledAssetSerializer

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        try:
            orders = Order.objects.all()
            page = self.paginate_queryset(orders)
            if page is not None:
                serializer = OrderSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = OrderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            order = Order.objects.get(id=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({'Error': f'Order with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            order = Order.objects.get(id=pk)
            serializer = OrderSerializer(instance=order, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Order.DoesNotExist:
            return Response({'Error': f'Order with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            order = Order.objects.get(id=pk)
            order.delete()
            return Response({'Response': f'Order with id {pk} succesfully deleted.'}, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({'Error': f'Order with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def search(self, request):
        try:
            search_params = request.GET.copy()
            search_params.pop('limit','')
            search_params.pop('offset','')
            arguments = {}
            if len(search_params) == 0:
                arguments['null'] = 'null'
            else:
                for k, v in search_params.items():
                    if v.startswith("r'"):
                        arguments[k + '__regex'] = v[2:-1]
                    else:
                        arguments[k] = v
            orders = Order.objects.filter(**arguments)
            page = self.paginate_queryset(orders)
            if page is not None:
                serializer = OrderSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
        except FieldError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        try:
            order_items = OrderItem.objects.all()
            page = self.paginate_queryset(order_items)
            if page is not None:
                serializer = OrderItemSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = OrderItemSerializer(order_items, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = OrderItemSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            order_item = OrderItem.objects.get(id=pk)
            serializer = OrderItemSerializer(order_item)
            return Response(serializer.data)
        except OrderItem.DoesNotExist:
            return Response({'Error': f'Order Item with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            order_item = OrderItem.objects.get(id=pk)
            serializer = OrderItemSerializer(instance=order_item, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except OrderItem.DoesNotExist:
            return Response({'Error': f'Order Item with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            order_item = OrderItem.objects.get(id=pk)
            order_item.delete()
            return Response({'Response': f'Order Item with id {pk} succesfully deleted.'}, status=status.HTTP_200_OK)
        except OrderItem.DoesNotExist:
            return Response({'Error': f'Order Item with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
    def search(self, request):
        try:
            search_params = request.GET.copy()
            search_params.pop('limit','')
            search_params.pop('offset','')
            arguments = {}
            if len(search_params) == 0:
                arguments['null'] = 'null'
            else:
                for k, v in search_params.items():
                    if v.startswith("r'"):
                        arguments[k + '__regex'] = v[2:-1]
                    else:
                        arguments[k] = v
            order_items = OrderItem.objects.filter(**arguments)
            page = self.paginate_queryset(order_items)
            if page is not None:
                serializer = OrderItemSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = OrderItemSerializer(order_items, many=True)
            return Response(serializer.data)
        except FieldError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class InstalledAssetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        try:
            assets = InstalledAsset.objects.all()
            page = self.paginate_queryset(assets)
            if page is not None:
                serializer = InstalledAssetSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = InstalledAssetSerializer(assets, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = InstalledAssetSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            asset = InstalledAsset.objects.get(id=pk)
            serializer = InstalledAssetSerializer(asset)
            return Response(serializer.data)
        except InstalledAsset.DoesNotExist:
            return Response({'Error': f'Installed Asset with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            asset = InstalledAsset.objects.get(id=pk)
            serializer = InstalledAssetSerializer(instance=asset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except InstalledAsset.DoesNotExist:
            return Response({'Error': f'Installed Asset with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            asset = InstalledAsset.objects.get(id=pk)
            asset.delete()
            return Response({'Response': f'Installed Asset with id {pk} succesfully deleted.'}, status=status.HTTP_200_OK)
        except InstalledAsset.DoesNotExist:
            return Response({'Error': f'Installed Asset with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
                       
    def search(self, request):
        try:
            arguments = {}
            search_params = request.GET.copy()
            search_params.pop('limit','')
            search_params.pop('offset','')
            if len(search_params) == 0:
                arguments['null'] = 'null'
            else:
                for k, v in search_params.items():
                    if v.startswith("r'"):
                        arguments[k + '__regex'] = v[2:-1]
                    else:
                        arguments[k] = v
            assets = InstalledAsset.objects.filter(**arguments)
            page = self.paginate_queryset(assets)
            if page is not None:
                serializer = InstalledAssetSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = InstalledAssetSerializer(assets, many=True)
            return Response(serializer.data)
        except FieldError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)