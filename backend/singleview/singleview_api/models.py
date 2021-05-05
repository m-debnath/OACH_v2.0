from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
import datetime
from dateutil.relativedelta import relativedelta

def date_age_validator(value):
    min_date = datetime.date.today() - relativedelta(years=100)
    max_date = datetime.date.today() - relativedelta(years=18)
    if value > max_date or value < min_date:
        raise ValidationError('Person must be between 18 and 100 years old.')

def date_slt_validator(value):
    min_date = datetime.date.today()
    if value < min_date:
        raise ValidationError('Group SLT can not be in past.')

class Account(models.Model):
    AccountNumber = models.CharField(max_length=50)
    AccountSSN = models.CharField(max_length=50)
    AccountName = models.CharField(max_length=255)
    AccountClass = models.CharField(max_length=30)
    AccountType = models.CharField(max_length=30)
    AccountSubType = models.CharField(max_length=30)
    AccountCreditLimit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)])
    ParentAccountId = models.CharField(max_length=15, blank=True, null=True)
    RootAccountId = models.CharField(max_length=15, blank=True, null=True)
    AccountEmailAddress = models.EmailField(max_length=100)
    AccountMobile = models.EmailField(max_length=20)
    AccountDateOfBirth = models.DateField(validators=[date_age_validator])
    AccountAddress = models.CharField(max_length=500)
    AccountStatus = models.EmailField(max_length=30)
    AccountStanding = models.EmailField(max_length=30)
        
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return f'{self.AccountType} {self.AccountClass} Account - {self.AccountName} with Account # {self.AccountNumber}'

class Activity(models.Model):
    ActivityAccountId = models.CharField(max_length=15)
    ActivityOrderId = models.CharField(max_length=15, null=True, blank=True)
    ActivityAssetId = models.CharField(max_length=15, null=True, blank=True)
    ActivitySRId = models.CharField(max_length=15, null=True, blank=True)
    ActivityInvoiceId = models.CharField(max_length=15, null=True, blank=True)
    ActivityType = models.CharField(max_length=30)
    ActivityCategory = models.CharField(max_length=30)
    ActivityStatus = models.CharField(max_length=30)
    ActivityOwner = models.CharField(max_length=100)
    ActivityDepartment = models.CharField(max_length=30)
    ActivityComment = models.TextField()
    ActivityDescription = models.TextField(null=True, blank=True)
    ActivitySLT = models.DateField(validators=[date_slt_validator])

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f'{self.ActivityCategory} - {self.ActivityType} Activity of {self.ActivityOwner} from {self.ActivityDepartment}'

class ServiceRequest(models.Model):
    ServiceRequestAccountId = models.CharField(max_length=15)
    ServiceRequestOrderId = models.CharField(max_length=15, null=True, blank=True)
    ServiceRequestAssetId = models.CharField(max_length=15, null=True, blank=True)
    ServiceRequestInvoiceId = models.CharField(max_length=15, null=True, blank=True)
    ServiceRequestProduct = models.CharField(max_length=30, null=True, blank=True)
    ServiceRequestType = models.CharField(max_length=30, null=True, blank=True)
    ServiceRequestArea = models.CharField(max_length=30, null=True, blank=True)
    ServiceRequestSubArea = models.CharField(max_length=30, null=True, blank=True)
    ServiceRequestResolutionCode = models.CharField(max_length=30, null=True, blank=True)
    ServiceRequestCaseLevel1 = models.CharField(max_length=30, null=True, blank=True)
    ServiceRequestCaseLevel2 = models.CharField(max_length=30, null=True, blank=True)
    ServiceRequestCaseLevel3 = models.CharField(max_length=30, null=True, blank=True)
    ServiceRequestStatus = models.CharField(max_length=30)
    ServiceRequestOwner = models.CharField(max_length=100)
    ServiceRequestDepartment = models.CharField(max_length=30)
    ServiceRequestComment = models.TextField(null=True, blank=True)
    ServiceRequestSLT = models.DateField(validators=[date_slt_validator])
    
    class Meta:
        verbose_name = 'Service Request'
        verbose_name_plural = 'Service Requests'

    def __str__(self):
        return f'{self.ServiceRequestProduct} - {self.ServiceRequestType} Service Request of {self.ServiceRequestOwner} from {self.ServiceRequestDepartment}'

class Invoice(models.Model):
    InvoiceAccountId = models.CharField(max_length=15)
    InvoiceAccountNumber = models.CharField(max_length=20)
    InvoiceNumber = models.CharField(max_length=15)
    InvoiceType = models.CharField(max_length=30)
    InvoiceStatus = models.CharField(max_length=30)
    InvoiceAmount = models.DecimalField(decimal_places=2,max_digits=10)
    InvoiceVatAmount = models.DecimalField(decimal_places=2,max_digits=10)
    InvoiceVatExclAmount = models.DecimalField(decimal_places=2,max_digits=10)
    DueAmount = models.DecimalField(decimal_places=2,max_digits=10)
    InvoiceDate = models.DateField()
    DueDate = models.DateField()
    DisputeOpenDate = models.DateField(null=True, blank=True)
    DisputeExpiryDate = models.DateField(null=True, blank=True)
    InvoiceURL = models.URLField(max_length=200)
    
    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        return f'Invoice # {self.InvoiceNumber} of Account Id {self.InvoiceAccountId}'

class Payment(models.Model):
    PaymentAccountId = models.CharField(max_length=15)
    PaymentInvoiceId = models.CharField(max_length=15)
    PaymentMemoNumber = models.CharField(max_length=50)
    PaymentType = models.CharField(max_length=30)
    PaymentStatus = models.CharField(max_length=30)
    PaymentAmount = models.DecimalField(decimal_places=2,max_digits=10)
    PaymentDate = models.DateField()    
    
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return f'Payment # {self.PaymentMemoNumber} of Account Id {self.PaymentAccountId}'

class Treatment(models.Model):
    TreatmentAccountId = models.CharField(max_length=15)
    TreatmentStage = models.CharField(max_length=30)
    TreatmentStatus = models.CharField(max_length=30)
    TreatmentOpenDate = models.DateField()    
    
    class Meta:
        verbose_name = 'Treatment'
        verbose_name_plural = 'Treatments'

    def __str__(self):
        return f'{self.TreatmentStatus} Treatment at Stage {self.TreatmentStage} of Account Id {self.TreatmentAccountId}'
