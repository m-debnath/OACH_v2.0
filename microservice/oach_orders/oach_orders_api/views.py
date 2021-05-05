from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Transaction, TransactionParameter
from datetime import datetime
from babel.dates import format_date
import requests
import uuid

class OrdersList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        locale = 'en_US'
        trans_name = 'Get Orders By Account Id'
        trans_url_param = 'RequestURL'
        trans_url_value = ''
        trans_auth_param = 'Authorization'
        trans_auth_value = ''
        trans_hdr_uuid_name = 'X-Servicedelivery-Request-Id'
        trans_hdr_uuid_value = request.META.get('HTTP_X_OACH_REQUEST_ID', uuid.uuid4().hex)
        try:
            backend_transactions = Transaction.objects.filter(TransactionName=trans_name)
            if (len(backend_transactions) == 0):
                raise Exception(f'Transaction - {trans_name} is not found.')
            try:
                trans_url_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_url_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_name} Request URL is not found.')
            try:
                trans_auth_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_auth_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_name} Authorization is not found.')
            if not trans_url_value:
                raise Exception(f'Transaction - {trans_name} Request URL is not found.')
            if not trans_auth_value:
                raise Exception(f'Transaction - {trans_name} Authorization is not found.')
            request_headers = {
                trans_auth_param: trans_auth_value,
                trans_hdr_uuid_name: trans_hdr_uuid_value
            }
            request_params = {}
            orders = []
            account_class = request.GET.get('AccountClass', '')
            if account_class != 'Customer' and account_class != 'Billing':
                raise Exception('AccountClass is mandatory. Possible values are Customer or Billing.')
            if account_class == 'Customer':
                request_params['CustomerAccountId'] = pk
            elif account_class == 'Billing':
                request_params['BillingAccountId'] = pk
            response = requests.get(trans_url_value, params=request_params, headers=request_headers)
            if response.ok:
                for order in response.json().get('results'):
                    orders.append(order)
                next_url = response.json().get('next')
                while next_url:
                    response = requests.get(next_url, headers=request_headers)
                    if response.ok:
                        for order in response.json().get('results'):
                            orders.append(order)
                        next_url = response.json().get('next')
                    else:
                        next_url = None
                        return Response(response.json(), status=response.status_code)
            else:
                return Response(response.json(), status=response.status_code)
            input_locale = request.GET.get('Locale', '')
            if input_locale == 'LVI':
                locale = 'lv_LV'
            elif input_locale == 'ETI':
                locale = 'et_EE'
            elif input_locale == 'LTH':
                locale = 'lt_LT'
            for order in orders:
                order['id'] = str(order['id'])
                if order['OrderDate']:
                    order['OrderDate'] = format_date(datetime.strptime(order['OrderDate'], '%Y-%m-%d'), "dd-MM-yyyy", locale=locale)

            # Start getting Order Items    
            trans_order_item_name = 'Get Order Items By Account Id'
            trans_url_value = ''
            trans_auth_value = ''
            backend_transactions = Transaction.objects.filter(TransactionName=trans_order_item_name)
            if (len(backend_transactions) == 0):
                raise Exception(f'Transaction - {trans_name} is not found.')
            try:
                trans_url_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_url_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_name} Request URL is not found.')
            try:
                trans_auth_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_auth_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_name} Authorization is not found.')
            if not trans_url_value:
                raise Exception(f'Transaction - {trans_name} Request URL is not found.')
            if not trans_auth_value:
                raise Exception(f'Transaction - {trans_name} Authorization is not found.')
            request_headers = {
                trans_auth_param: trans_auth_value,
                trans_hdr_uuid_name: trans_hdr_uuid_value
            }
            for order in orders:
                request_params = {}
                order_items = []
                request_params['OrderItemOrderId'] = order['id']
                response = requests.get(trans_url_value, params=request_params, headers=request_headers)
                if response.ok:
                    for order_item in response.json().get('results'):
                        order_items.append(order_item)
                    next_url = response.json().get('next')
                    while next_url:
                        response = requests.get(next_url, headers=request_headers)
                        if response.ok:
                            for order_item in response.json().get('results'):
                                order_items.append(order_item)
                            next_url = response.json().get('next')
                        else:
                            next_url = None
                            return Response(response.json(), status=response.status_code)
                else:
                    return Response(response.json(), status=response.status_code)
                for order_item in order_items:
                    order_item['id'] = str(order_item['id'])
                    if order_item['StatusDate']:
                        order_item['StatusDate'] = format_date(datetime.strptime(order_item['StatusDate'], '%Y-%m-%d'), locale=locale)
                    if order_item['ContractStartDate']:
                        order_item['ContractStartDate'] = format_date(datetime.strptime(order_item['ContractStartDate'], '%Y-%m-%d'), locale=locale)
                    if order_item['ContractEndDate']:
                        order_item['ContractEndDate'] = format_date(datetime.strptime(order_item['ContractEndDate'], '%Y-%m-%d'), locale=locale)
                    if order_item['RegretEndDate']:
                        order_item['RegretEndDate'] = format_date(datetime.strptime(order_item['RegretEndDate'], '%Y-%m-%d'), locale=locale)
                    if order_item['PlannedDisconnectDate']:
                        order_item['PlannedDisconnectDate'] = format_date(datetime.strptime(order_item['PlannedDisconnectDate'], '%Y-%m-%d'), locale=locale)
                    if order_item['DisconnectDate']:
                        order_item['DisconnectDate'] = format_date(datetime.strptime(order_item['DisconnectDate'], '%Y-%m-%d'), locale=locale)
                root_order_items = []
                for order_item in order_items:
                    if not order_item['ParentOrderItemId']:
                        root_order_items.append(order_item)
                for root_order_item in root_order_items:
                    first_level_children = []
                    for order_item in order_items:
                        if root_order_item['id'] == order_item['ParentOrderItemId']:
                            first_level_children.append(order_item)
                    if len(first_level_children) > 0:
                        root_order_item['children'] = first_level_children
                for root_order_item in root_order_items:
                    print('second level each root order item')
                    for first_level_child in root_order_item['children']:
                        print('second level each first level child order item')
                        second_level_children = []
                        for order_item in order_items:
                            if first_level_child['id'] == order_item['ParentOrderItemId']:
                                print('second level each first level child order item')
                                second_level_children.append(order_item)
                        if len(second_level_children) > 0:
                            first_level_child['children'] = second_level_children
                if len(root_order_items) > 0:
                    order['order_items'] = root_order_items
            return Response(orders, status=response.status_code)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)