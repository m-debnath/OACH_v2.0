from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Transaction, TransactionParameter
from datetime import datetime
from babel.dates import format_date
from babel.numbers import format_currency
import requests
import uuid

class AccountDetails(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        locale = 'en_US'
        currency = 'EUR'
        trans_name = 'Get Account By Id'
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
            response = requests.get(trans_url_value, headers=request_headers)
            if response.ok:
                account = response.json()
                input_locale = request.GET.get('Locale', '')
                if input_locale == 'LVI':
                    locale = 'lv_LV'
                elif input_locale == 'ETI':
                    locale = 'et_EE'
                elif input_locale == 'LTH':
                    locale = 'lt_LT'
                if account['AccountDateOfBirth']:
                    account['AccountDateOfBirth'] = format_date(datetime.strptime(account['AccountDateOfBirth'], '%Y-%m-%d'), locale=locale)
                if account['AccountCreditLimit']:
                    account['AccountCreditLimit'] = format_currency(account['AccountCreditLimit'], currency=currency, locale=locale)
                if account['AccountClass'] == 'Billing':
                    trans_name = 'Get Treatment By Billing Account Id'
                    request_params = {}
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
                    request_params = {
                        'TreatmentAccountId' : account['id']
                    }
                    request_headers = {
                        trans_auth_param: trans_auth_value,
                        trans_hdr_uuid_name: trans_hdr_uuid_value
                    }
                    response = requests.get(trans_url_value, params=request_params, headers=request_headers)
                    if response.ok:
                        treatment = response.json().get('results')[0]
                        if treatment['TreatmentOpenDate']:
                            treatment['TreatmentOpenDate'] = format_date(datetime.strptime(treatment['TreatmentOpenDate'], '%Y-%m-%d'), locale=locale)
                        account['treatment'] = treatment
                    else:
                        return Response(response.json(), status=response.status_code)
                return Response(account, status=response.status_code)
            else:
                return Response(response.json(), status=response.status_code)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def search(self, request, pk=None):
        locale = 'en_US'
        currency = 'EUR'
        trans_name = 'Search Account'
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
            request_params = {
                'AccountNumber' : pk
            }
            input_locale = request.GET.get('Locale', '')
            response = requests.get(trans_url_value, params=request_params, headers=request_headers)
            if response.ok:
                if int(response.json().get('count')) > 0:
                    account = response.json().get('results')[0]
                    account['id'] = str(account['id'])
                    if input_locale == 'LVI':
                        locale = 'lv_LV'
                    elif input_locale == 'ETI':
                        locale = 'et_EE'
                    elif input_locale == 'LTH':
                        locale = 'lt_LT'
                    if account['AccountDateOfBirth']:
                        account['AccountDateOfBirth'] = format_date(datetime.strptime(account['AccountDateOfBirth'], '%Y-%m-%d'), locale=locale)
                    if account['AccountCreditLimit']:
                        account['AccountCreditLimit'] = format_currency(account['AccountCreditLimit'], currency=currency, locale=locale)
                    return Response(account, status=response.status_code)
                else:
                    return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(response.json(), status=response.status_code)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        trans_name = 'Update Account By Id'
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

class AccountHierarchyDetails(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        locale = 'en_US'
        currency = 'EUR'
        trans_name = 'Get Account Hierarchy By Id'
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
            response = requests.get(trans_url_value, headers=request_headers)
            if response.ok:
                account_reponse = []
                account_hierarchy = {}
                account_children = []
                account_child = {}
                for account in response.json().get('results'):
                    account_reponse.append(account)                
                input_locale = request.GET.get('Locale', '')
                input_locale = request.GET.get('Locale', '')
                if input_locale == 'LVI':
                    locale = 'lv_LV'
                elif input_locale == 'ETI':
                    locale = 'et_EE'
                elif input_locale == 'LTH':
                    locale = 'lt_LT'
                for account in account_reponse:
                    account['id'] = str(account['id'])
                    if account['AccountDateOfBirth']:
                        account['AccountDateOfBirth'] = format_date(datetime.strptime(account['AccountDateOfBirth'], '%Y-%m-%d'), locale=locale)
                    if account['AccountCreditLimit']:
                        account['AccountCreditLimit'] = format_currency(account['AccountCreditLimit'], currency=currency, locale=locale)
                    if account['AccountClass'] == 'Billing':
                        trans_name = 'Get Treatment By Billing Account Id'
                        request_params = {}
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
                        request_params = {
                            'TreatmentAccountId' : account['id']
                        }
                        request_headers = {
                            trans_auth_param: trans_auth_value,
                            trans_hdr_uuid_name: trans_hdr_uuid_value
                        }
                        response = requests.get(trans_url_value, params=request_params, headers=request_headers)
                        if response.ok:
                            if response.json().get('count') > 0:
                                treatment = response.json().get('results')[0]
                                if treatment['TreatmentOpenDate']:
                                    treatment['TreatmentOpenDate'] = format_date(datetime.strptime(treatment['TreatmentOpenDate'], '%Y-%m-%d'), locale=locale)
                                account['treatment'] = treatment
                        else:
                            return Response(response.json(), status=response.status_code)
                for account in account_reponse:
                    if account.get('id') == account.get('RootAccountId'):
                        account_hierarchy = account
                    else:
                        account_child = account
                        account_children.append(account_child)
                if (len(account_children) > 0):
                    account_hierarchy['children'] = account_children
                return Response(account_hierarchy, status=response.status_code)
            else:
                return Response(response.json(), status=response.status_code)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)