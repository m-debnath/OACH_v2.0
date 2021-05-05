from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import FieldError
from .models import Account, Activity, ServiceRequest, Invoice, Payment, Treatment
from .serializers import AccountSerializer, ActivitySerializer, ServiceRequestSerializer, InvoiceSerializer, PaymentSerializer, TreatmentSerializer

class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        try:
            accounts = Account.objects.all()
            page = self.paginate_queryset(accounts)
            if page is not None:
                serializer = AccountSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = AccountSerializer(accounts, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = AccountSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            account = Account.objects.get(id=pk)
            serializer = AccountSerializer(account)
            return Response(serializer.data)
        except Account.DoesNotExist:
            return Response({'Error': f'Account with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            account = Account.objects.get(id=pk)
            serializer = AccountSerializer(instance=account, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Account.DoesNotExist:
            return Response({'Error': f'Account with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            account = Account.objects.get(id=pk)
            account.delete()
            return Response({'Response': f'Account with id {pk} succesfully deleted.'}, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({'Error': f'Account with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
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
            accounts = Account.objects.filter(**arguments)
            page = self.paginate_queryset(accounts)
            if page is not None:
                serializer = AccountSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = AccountSerializer(accounts, many=True)
            return Response(serializer.data)
        except FieldError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ActivityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        try:
            activities = Activity.objects.all()
            page = self.paginate_queryset(activities)
            if page is not None:
                serializer = ActivitySerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = ActivitySerializer(activities, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = ActivitySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            activity = Activity.objects.get(id=pk)
            serializer = ActivitySerializer(activity)
            return Response(serializer.data)
        except Activity.DoesNotExist:
            return Response({'Error': f'Activity with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            activity = Activity.objects.get(id=pk)
            serializer = ActivitySerializer(instance=activity, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Activity.DoesNotExist:
            return Response({'Error': f'Activity with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            activity = Activity.objects.get(id=pk)
            activity.delete()
            return Response({'Response': f'Activity with id {pk} succesfully deleted.'}, status=status.HTTP_200_OK)
        except Activity.DoesNotExist:
            return Response({'Error': f'Activity with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
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
            activities = Activity.objects.filter(**arguments)
            page = self.paginate_queryset(activities)
            if page is not None:
                serializer = ActivitySerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = ActivitySerializer(activities, many=True)
            return Response(serializer.data)
        except FieldError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ServiceRequestViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        try:
            service_requests = ServiceRequest.objects.all()
            page = self.paginate_queryset(service_requests)
            if page is not None:
                serializer = ServiceRequestSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = ServiceRequestSerializer(service_requests, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = ServiceRequestSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            service_request = ServiceRequest.objects.get(id=pk)
            serializer = ServiceRequestSerializer(service_request)
            return Response(serializer.data)
        except ServiceRequest.DoesNotExist:
            return Response({'Error': f'Service Request with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            service_request = ServiceRequest.objects.get(id=pk)
            serializer = ServiceRequestSerializer(instance=service_request, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except ServiceRequest.DoesNotExist:
            return Response({'Error': f'Service Request with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            service_request = ServiceRequest.objects.get(id=pk)
            service_request.delete()
            return Response({'Response': f'Service Request with id {pk} succesfully deleted.'}, status=status.HTTP_200_OK)
        except ServiceRequest.DoesNotExist:
            return Response({'Error': f'Service Request with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
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
            service_requests = ServiceRequest.objects.filter(**arguments)
            page = self.paginate_queryset(service_requests)
            if page is not None:
                serializer = ServiceRequestSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = ServiceRequestSerializer(service_requests, many=True)
            return Response(serializer.data)
        except FieldError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class InvoiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        try:
            invoices = Invoice.objects.all()
            page = self.paginate_queryset(invoices)
            if page is not None:
                serializer = InvoiceSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = InvoiceSerializer(invoices, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = InvoiceSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            invoice = Invoice.objects.get(id=pk)
            serializer = InvoiceSerializer(invoice)
            return Response(serializer.data)
        except Invoice.DoesNotExist:
            return Response({'Error': f'Invoice with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            invoice = Invoice.objects.get(id=pk)
            serializer = InvoiceSerializer(instance=invoice, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Invoice.DoesNotExist:
            return Response({'Error': f'Invoice with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            invoice = Invoice.objects.get(id=pk)
            invoice.delete()
            return Response({'Response': f'Invoice with id {pk} succesfully deleted.'}, status=status.HTTP_200_OK)
        except Invoice.DoesNotExist:
            return Response({'Error': f'Invoice with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
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
            invoices = Invoice.objects.filter(**arguments)
            page = self.paginate_queryset(invoices)
            if page is not None:
                serializer = InvoiceSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = InvoiceSerializer(invoices, many=True)
            return Response(serializer.data)
        except FieldError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        try:
            payments = Payment.objects.all()
            page = self.paginate_queryset(payments)
            if page is not None:
                serializer = PaymentSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = PaymentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            payment = Payment.objects.get(id=pk)
            serializer = PaymentSerializer(payment)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response({'Error': f'Payment with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            payment = Payment.objects.get(id=pk)
            serializer = PaymentSerializer(instance=payment, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Payment.DoesNotExist:
            return Response({'Error': f'Payment with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            payment = Payment.objects.get(id=pk)
            payment.delete()
            return Response({'Response': f'Payment with id {pk} succesfully deleted.'}, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({'Error': f'Payment with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
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
            payments = Payment.objects.filter(**arguments)
            page = self.paginate_queryset(payments)
            if page is not None:
                serializer = PaymentSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            if len(payments) == 0:
                return Response({'Response': 'Payment not found.'}, status=status.HTTP_404_NOT_FOUND)
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data)
        except FieldError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class TreatmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        try:
            treatments = Treatment.objects.all()
            page = self.paginate_queryset(treatments)
            if page is not None:
                serializer = TreatmentSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = TreatmentSerializer(treatments, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = TreatmentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            treatment = Treatment.objects.get(id=pk)
            serializer = TreatmentSerializer(treatment)
            return Response(serializer.data)
        except Treatment.DoesNotExist:
            return Response({'Error': f'Treatment with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            treatment = Treatment.objects.get(id=pk)
            serializer = TreatmentSerializer(instance=treatment, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Treatment.DoesNotExist:
            return Response({'Error': f'Treatment with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            treatment = Treatment.objects.get(id=pk)
            treatment.delete()
            return Response({'Response': f'Treatment with id {pk} succesfully deleted.'}, status=status.HTTP_200_OK)
        except Treatment.DoesNotExist:
            return Response({'Error': f'Treatment with id {pk} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
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
            treatments = Treatment.objects.filter(**arguments)
            page = self.paginate_queryset(treatments)
            if page is not None:
                serializer = TreatmentSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = TreatmentSerializer(treatments, many=True)
            return Response(serializer.data)
        except FieldError as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)