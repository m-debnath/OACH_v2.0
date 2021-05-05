from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Transaction, TransactionParameter
from datetime import datetime
from babel.dates import format_date
import requests
import uuid

class AssetList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        locale = 'en_US'
        trans_name = 'Get Assets By Account Id'
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
            asset_list = []
            account_class = request.GET.get('AccountClass', '')
            if account_class != 'Customer' and account_class != 'Billing':
                raise Exception('AccountClass is mandatory. Possible values are Customer or Billing.')
            if account_class == 'Customer':
                request_params['CustomerAccountId'] = pk
            elif account_class == 'Billing':
                request_params['BillingAccountId'] = pk
            response = requests.get(trans_url_value, params=request_params, headers=request_headers)
            if response.ok:
                for asset in response.json().get('results'):
                    asset_list.append(asset)
                next_url = response.json().get('next')
                while next_url:
                    response = requests.get(next_url, headers=request_headers)
                    if response.ok:
                        for asset in response.json().get('results'):
                            asset_list.append(asset)
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
            for asset in asset_list:
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
            root_assets = []
            for asset in asset_list:
                if not asset['ParentAssetId']:
                    root_assets.append(asset)
            for root_asset in root_assets:
                first_level_children = []
                for asset in asset_list:
                    if root_asset['id'] == asset['ParentAssetId']:
                        first_level_children.append(asset)
                if len(first_level_children) > 0:
                    root_asset['children'] = first_level_children
            for root_asset in root_assets:
                if 'children' in root_asset:
                    for first_level_child in root_asset['children']:
                        second_level_children = []
                        for asset in asset_list:
                            if first_level_child['id'] == asset['ParentAssetId']:
                                second_level_children.append(asset)
                        if len(second_level_children) > 0:
                            first_level_child['children'] = second_level_children
            return Response(root_assets, status=response.status_code)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AssetPAVList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        locale = 'en_US'
        trans_name = 'Get Assets By Account Id'
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
            asset_list = []
            request_params['PrimaryAttributeValue'] = pk
            response = requests.get(trans_url_value, params=request_params, headers=request_headers)
            if response.ok:
                for asset in response.json().get('results'):
                    asset_list.append(asset)
                next_url = response.json().get('next')
                while next_url:
                    response = requests.get(next_url, headers=request_headers)
                    if response.ok:
                        for asset in response.json().get('results'):
                            asset_list.append(asset)
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
            for asset in asset_list:
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
            root_assets = []
            for asset in asset_list:
                if not asset['ParentAssetId']:
                    root_assets.append(asset)
            for root_asset in root_assets:
                first_level_children = []
                for asset in asset_list:
                    if root_asset['id'] == asset['ParentAssetId']:
                        first_level_children.append(asset)
                if len(first_level_children) > 0:
                    root_asset['children'] = first_level_children
            for root_asset in root_assets:
                if 'children' in root_asset:
                    for first_level_child in root_asset['children']:
                        second_level_children = []
                        for asset in asset_list:
                            if first_level_child['id'] == asset['ParentAssetId']:
                                second_level_children.append(asset)
                        if len(second_level_children) > 0:
                            first_level_child['children'] = second_level_children
            return Response(root_assets, status=response.status_code)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)