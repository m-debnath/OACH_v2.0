from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Transaction, TransactionParameter
from datetime import datetime
from babel.dates import format_date
from babel.numbers import format_currency
import requests
import uuid

class InvoicesList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        locale = 'en_US'
        currency = 'EUR'
        trans_name = 'Get Invoice By Billing Account Id'
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
            request_params = {}
            invoices = []
            request_params['InvoiceAccountId'] = pk
            response = requests.get(trans_url_value, params=request_params, headers=request_headers)
            if response.ok:
                for invoice in response.json().get('results'):
                    invoices.append(invoice)
                next_url = response.json().get('next')
                while next_url:
                    response = requests.get(next_url, headers=request_headers)
                    if response.ok:
                        for invoice in response.json().get('results'):
                            invoices.append(invoice)
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
            for invoice in invoices:
                invoice['id'] = str(invoice['id'])
                if invoice['InvoiceDate']:
                    invoice['InvoiceLongDate'] = format_date(datetime.strptime(invoice['InvoiceDate'], '%Y-%m-%d'), "MMMM, ''yy", locale='en_US').capitalize()
                    invoice['InvoiceDate'] = format_date(datetime.strptime(invoice['InvoiceDate'], '%Y-%m-%d'), "MMM ''yy", locale='en_US').capitalize()
                if invoice['DueDate']:
                    invoice['DueDate'] = format_date(datetime.strptime(invoice['DueDate'], '%Y-%m-%d'), "dd-MM-yyyy", locale=locale)
                if invoice['DisputeOpenDate']:
                    invoice['DisputeOpenDate'] = format_date(datetime.strptime(invoice['DisputeOpenDate'], '%Y-%m-%d'), "dd-MM-yyyy", locale=locale)
                if invoice['DisputeExpiryDate']:
                    invoice['DisputeExpiryDate'] = format_date(datetime.strptime(invoice['DisputeExpiryDate'], '%Y-%m-%d'), "dd-MM-yyyy", locale=locale)
                if invoice['InvoiceAmount']:
                    invoice['InvoiceNumericAmount'] = invoice['InvoiceAmount']
                    invoice['InvoiceAmount'] = format_currency(invoice['InvoiceAmount'], currency=currency, locale=locale)
                if invoice['InvoiceVatAmount']:
                    invoice['InvoiceVatAmount'] = format_currency(invoice['InvoiceVatAmount'], currency=currency, locale=locale)
                if invoice['InvoiceVatExclAmount']:
                    invoice['InvoiceVatExclAmount'] = format_currency(invoice['InvoiceVatExclAmount'], currency=currency, locale=locale)
                if invoice['DueAmount']:
                    invoice['DueAmount'] = format_currency(invoice['DueAmount'], currency=currency, locale=locale)

            # Start getting Payments
            trans_payments_name = 'Get Payments By Invoice Id'
            trans_url_value = ''
            trans_auth_value = ''
            backend_transactions = Transaction.objects.filter(TransactionName=trans_payments_name)
            if (len(backend_transactions) == 0):
                raise Exception(f'Transaction - {trans_payments_name} is not found.')
            try:
                trans_url_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_url_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_payments_name} Request URL is not found.')
            try:
                trans_auth_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_auth_param).first().ParameterValue
            except Exception:
                raise Exception(f'Transaction - {trans_payments_name} Authorization is not found.')
            if not trans_url_value:
                raise Exception(f'Transaction - {trans_payments_name} Request URL is not found.')
            if not trans_auth_value:
                raise Exception(f'Transaction - {trans_payments_name} Authorization is not found.')
            request_headers = {
                trans_auth_param: trans_auth_value,
                trans_hdr_uuid_name: trans_hdr_uuid_value
            }
            for invoice in invoices:
                request_params = {}
                payments = []
                request_params['PaymentInvoiceId'] = invoice['id']
                response = requests.get(trans_url_value, params=request_params, headers=request_headers)
                if response.ok:
                    for payment in response.json().get('results'):
                        payments.append(payment)
                    next_url = response.json().get('next')
                    while next_url:
                        response = requests.get(next_url, headers=request_headers)
                        if response.ok:
                            for payment in response.json().get('results'):
                                payments.append(payment)
                            next_url = response.json().get('next')
                        else:
                            next_url = None
                            return Response(response.json(), status=response.status_code)
                else:
                    return Response(response.json(), status=response.status_code)
                for payment in payments:
                    payment['id'] = str(payment['id'])
                    if payment['PaymentDate']:
                        payment['PaymentDate'] = format_date(datetime.strptime(payment['PaymentDate'], '%Y-%m-%d'), locale=locale)
                    if payment['PaymentAmount']:
                        payment['PaymentAmount'] = format_currency(payment['PaymentAmount'], currency=currency, locale=locale)
                if len(payments) > 0:
                    invoice['payments'] = payments
            return Response(invoices, status=response.status_code)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)