from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Transaction, TransactionParameter
from datetime import datetime
from babel.dates import format_date
from babel.numbers import format_currency
import requests
import uuid

class ActivitiesList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        locale = 'en_US'
        currency = 'EUR'
        trans_name = 'Get Activities By Account Id'
        trans_url_param = 'RequestURL'
        trans_url_value = ''
        trans_auth_param = 'Authorization'
        trans_auth_value = ''
        trans_hdr_uuid_name = 'X-Singleview-Request-Id'
        trans_hdr_sd_uuid_name = 'X-Servicedelivery-Request-Id'
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
            activities = []
            request_params['ActivityAccountId'] = pk
            response = requests.get(trans_url_value, params=request_params, headers=request_headers)
            if response.ok:
                for activity in response.json().get('results'):
                    activities.append(activity)
                next_url = response.json().get('next')
                while next_url:
                    response = requests.get(next_url, headers=request_headers)
                    if response.ok:
                        for activity in response.json().get('results'):
                            activities.append(activity)
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
            for activity in activities:
                activity['id'] = str(activity['id'])
                if activity['ActivitySLT']:
                    activity['ActivitySLT'] = format_date(datetime.strptime(activity['ActivitySLT'], '%Y-%m-%d'), locale=locale)

            # Getting Account Transaction details
            trans_accounts_name = 'Get Account By Id'
            trans_accounts_url_value = ''
            trans_accounts_auth_value = ''
            backend_transactions = Transaction.objects.filter(TransactionName=trans_accounts_name)
            if (len(backend_transactions) == 0):
                raise Exception(f'Transaction - {trans_accounts_name} is not found.')
            try:
                trans_accounts_url_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_url_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_accounts_name} Request URL is not found.')
            try:
                trans_accounts_auth_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_auth_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_accounts_name} Authorization is not found.')
            if not trans_accounts_url_value:
                raise Exception(f'Transaction - {trans_accounts_name} Request URL is not found.')
            if not trans_accounts_auth_value:
                raise Exception(f'Transaction - {trans_accounts_name} Authorization is not found.')
            request_accounts_headers = {
                trans_auth_param: trans_accounts_auth_value,
                trans_hdr_uuid_name: trans_hdr_uuid_value
            }
            # Getting Asset Transaction details
            trans_assets_name = 'Get Asset By Id'
            trans_assets_url_value = ''
            trans_assets_auth_value = ''
            backend_transactions = Transaction.objects.filter(TransactionName=trans_assets_name)
            if (len(backend_transactions) == 0):
                raise Exception(f'Transaction - {trans_assets_name} is not found.')
            try:
                trans_assets_url_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_url_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_assets_name} Request URL is not found.')
            try:
                trans_assets_auth_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_auth_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_assets_name} Authorization is not found.')
            if not trans_assets_url_value:
                raise Exception(f'Transaction - {trans_assets_name} Request URL is not found.')
            if not trans_assets_auth_value:
                raise Exception(f'Transaction - {trans_assets_name} Authorization is not found.')
            request_assets_headers = {
                trans_auth_param: trans_assets_auth_value,
                trans_hdr_sd_uuid_name: trans_hdr_uuid_value
            }
            # Getting Order Transaction details
            trans_orders_name = 'Get Order By Id'
            trans_orders_url_value = ''
            trans_orders_auth_value = ''
            backend_transactions = Transaction.objects.filter(TransactionName=trans_orders_name)
            if (len(backend_transactions) == 0):
                raise Exception(f'Transaction - {trans_orders_name} is not found.')
            try:
                trans_orders_url_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_url_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_orders_name} Request URL is not found.')
            try:
                trans_orders_auth_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_auth_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_orders_name} Authorization is not found.')
            if not trans_orders_url_value:
                raise Exception(f'Transaction - {trans_orders_name} Request URL is not found.')
            if not trans_orders_auth_value:
                raise Exception(f'Transaction - {trans_orders_name} Authorization is not found.')
            request_orders_headers = {
                trans_auth_param: trans_orders_auth_value,
                trans_hdr_sd_uuid_name: trans_hdr_uuid_value
            }
            # Getting Invoice Transaction details
            trans_invoices_name = 'Get Invoice By Id'
            trans_invoices_url_value = ''
            trans_invoices_auth_value = ''
            backend_transactions = Transaction.objects.filter(TransactionName=trans_invoices_name)
            if (len(backend_transactions) == 0):
                raise Exception(f'Transaction - {trans_invoices_name} is not found.')
            try:
                trans_invoices_url_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_url_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_invoices_name} Request URL is not found.')
            try:
                trans_invoices_auth_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_auth_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_invoices_name} Authorization is not found.')
            if not trans_invoices_url_value:
                raise Exception(f'Transaction - {trans_invoices_name} Request URL is not found.')
            if not trans_invoices_auth_value:
                raise Exception(f'Transaction - {trans_invoices_name} Authorization is not found.')
            request_invoices_headers = {
                trans_auth_param: trans_invoices_auth_value,
                trans_hdr_uuid_name: trans_hdr_uuid_value
            }
            # Getting Service Request Transaction details
            trans_service_requests_name = 'Get Service Request By Id'
            trans_service_requests_url_value = ''
            trans_service_requests_auth_value = ''
            backend_transactions = Transaction.objects.filter(TransactionName=trans_service_requests_name)
            if (len(backend_transactions) == 0):
                raise Exception(f'Transaction - {trans_service_requests_name} is not found.')
            try:
                trans_service_requests_url_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_url_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_service_requests_name} Request URL is not found.')
            try:
                trans_service_requests_auth_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_auth_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_service_requests_name} Authorization is not found.')
            if not trans_service_requests_url_value:
                raise Exception(f'Transaction - {trans_service_requests_name} Request URL is not found.')
            if not trans_service_requests_auth_value:
                raise Exception(f'Transaction - {trans_service_requests_name} Authorization is not found.')
            request_service_requests_headers = {
                trans_auth_param: trans_service_requests_auth_value,
                trans_hdr_uuid_name: trans_hdr_uuid_value
            }
            for activity in activities:
                # Get related account
                if activity['ActivityAccountId']:
                    trans_accounts_url_value = trans_accounts_url_value.replace('<pk>', activity['ActivityAccountId'])
                    response = requests.get(trans_accounts_url_value, headers=request_accounts_headers)
                    if response.ok:
                        account = response.json()
                        account['id'] = str(account['id'])
                        if account['AccountDateOfBirth']:
                            account['AccountDateOfBirth'] = format_date(datetime.strptime(account['AccountDateOfBirth'], '%Y-%m-%d'), locale=locale)
                        activity['account'] = account
                    else:
                        return Response(response.json(), status=response.status_code)
                # Get related order
                if activity['ActivityOrderId']:
                    trans_orders_url_value = trans_orders_url_value.replace('<pk>', activity['ActivityOrderId'])
                    response = requests.get(trans_orders_url_value, headers=request_orders_headers)
                    if response.ok:
                        order = response.json()
                        order['id'] = str(order['id'])
                        if order['OrderDate']:
                            order['OrderDate'] = format_date(datetime.strptime(order['OrderDate'], '%Y-%m-%d'), locale=locale)
                        activity['order'] = order
                    else:
                        return Response(response.json(), status=response.status_code)
                # Get related asset
                if activity['ActivityAssetId']:
                    trans_assets_url_value = trans_assets_url_value.replace('<pk>', activity['ActivityAssetId'])
                    response = requests.get(trans_assets_url_value, headers=request_assets_headers)
                    if response.ok:
                        asset = response.json()
                        asset['id'] = str(asset['id'])
                        if asset['ActualStartDate']:
                            asset['ActualStartDate'] = format_date(datetime.strptime(asset['ActualStartDate'], '%Y-%m-%d'), locale=locale)
                        if asset['ContractStartDate']:
                            asset['ContractStartDate'] = format_date(datetime.strptime(asset['ContractStartDate'], '%Y-%m-%d'), locale=locale)
                        if asset['ContractEndDate']:
                            asset['ContractEndDate'] = format_date(datetime.strptime(asset['ContractEndDate'], '%Y-%m-%d'), locale=locale)
                        if asset['RegretEndDate']:
                            asset['RegretEndDate'] = format_date(datetime.strptime(asset['RegretEndDate'], '%Y-%m-%d'), locale=locale)
                        if asset['PlannedDisconnectDate']:
                            asset['PlannedDisconnectDate'] = format_date(datetime.strptime(asset['PlannedDisconnectDate'], '%Y-%m-%d'), locale=locale)
                        if asset['ActualEndDate']:
                            asset['ActualEndDate'] = format_date(datetime.strptime(asset['ActualEndDate'], '%Y-%m-%d'), locale=locale)
                        activity['asset'] = asset
                    else:
                        return Response(response.json(), status=response.status_code)
                # Get related service request
                if activity['ActivitySRId']:
                    trans_service_requests_url_value = trans_service_requests_url_value.replace('<pk>', activity['ActivitySRId'])
                    response = requests.get(trans_service_requests_url_value, headers=request_service_requests_headers)
                    if response.ok:
                        service_request = response.json()
                        service_request['id'] = str(service_request['id'])
                        if service_request['ServiceRequestSLT']:
                            service_request['ServiceRequestSLT'] = format_date(datetime.strptime(service_request['ServiceRequestSLT'], '%Y-%m-%d'), locale=locale)
                        activity['service_request'] = service_request
                    else:
                        return Response(response.json(), status=response.status_code)
                # Get related invoice
                if activity['ActivityInvoiceId']:
                    trans_invoices_url_value = trans_invoices_url_value.replace('<pk>', activity['ActivityInvoiceId'])
                    response = requests.get(trans_invoices_url_value, headers=request_invoices_headers)
                    if response.ok:
                        invoice = response.json()
                        invoice['id'] = str(invoice['id'])
                        if invoice['InvoiceDate']:
                            invoice['InvoiceDate'] = format_date(datetime.strptime(invoice['InvoiceDate'], '%Y-%m-%d'), locale=locale)
                        if invoice['InvoiceAmount']:
                            invoice['InvoiceAmount'] = format_currency(invoice['InvoiceAmount'], currency=currency, locale=locale)
                        activity['invoice'] = invoice
                    else:
                        return Response(response.json(), status=response.status_code)
            return Response(activities, status=response.status_code)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ActivityDetails(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request, pk=None):
        trans_name = 'Create Activity'
        trans_url_param = 'RequestURL'
        trans_url_value = ''
        trans_auth_param = 'Authorization'
        trans_auth_value = ''
        trans_hdr_uuid_name = 'X-Singleview-Request-Id'
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
            response = requests.post(trans_url_value, data=request.data, headers=request_headers)
            return Response(response.json(), status=response.status_code)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        trans_name = 'Update Activity By Id'
        trans_url_param = 'RequestURL'
        trans_url_value = ''
        trans_auth_param = 'Authorization'
        trans_auth_value = ''
        trans_hdr_uuid_name = 'X-Singleview-Request-Id'
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
            trans_url_value = trans_url_value.replace('<pk>', pk)
            request_headers = {
                trans_auth_param: trans_auth_value,
                trans_hdr_uuid_name: trans_hdr_uuid_value
            }
            response = requests.put(trans_url_value, data=request.data, headers=request_headers)
            return Response(response.json(), status=response.status_code)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)